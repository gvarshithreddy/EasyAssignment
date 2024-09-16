import tkinter as tk
import multiprocessing
from datetime import datetime
import os
import sys
from gemini import generate_summary
from screenshot import ScreenshotApp
from dotenv import load_dotenv
load_dotenv('.env')
if not os.path.exists(os.getenv("ANSWER_SAVE_FOLDER")):
    os.makedirs(os.getenv("ANSWER_SAVE_FOLDER"))
# Define the function for the ScreenshotApp
def run_screenshot_app(queue, stop_event):
    root = tk.Tk()
    app = ScreenshotApp(root)

    def on_screenshot(screenshot_path):
        # When a screenshot is taken, add the path to the queue
        queue.put(screenshot_path)

    # Assuming your ScreenshotApp has a way to register a callback when a screenshot is taken
    app.set_screenshot_callback(on_screenshot)

    def check_stop_event():
        if stop_event.is_set():
            root.quit()
        else:
            root.after(100, check_stop_event)

    root.after(100, check_stop_event)
    root.mainloop()

# Function to generate summaries from the screenshots
def generate_summaries(queue, stop_event):
    print("Waiting for screenshots...")
    while not stop_event.is_set():
        try:
            # Wait for screenshot paths in the queue
            screenshot_path = queue.get(timeout=1)  # Timeout to check for stop_event regularly
            if screenshot_path:
                text = generate_summary(os.path.normpath(screenshot_path),os.getenv('ANSWER_FILE_PATH'), length="300")
        except multiprocessing.queues.Empty:
            # If no screenshot is in the queue, continue checking
            print("No screenshot in the queue.")
            continue
        except Exception as e:
            print(f"Error: {e}")
    print("Stopped generating summaries.")

class ApplicationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Screenshot and Summary App")
        master.geometry("300x150")

        self.start_button = tk.Button(master, text="Start", command=self.start_processes, height=2, width=20)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_processes, height=2, width=20, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.screenshot_process = None
        self.summary_process = None
        self.stop_event = multiprocessing.Event()
        self.queue = multiprocessing.Queue()

    def start_processes(self):
        self.stop_event.clear()

        # Create two processes: one for screenshotting and one for summary generation
        self.screenshot_process = multiprocessing.Process(target=run_screenshot_app, args=(self.queue, self.stop_event))
        self.summary_process = multiprocessing.Process(target=generate_summaries, args=(self.queue, self.stop_event))

        self.screenshot_process.start()
        self.summary_process.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_processes(self):
        self.stop_event.set()

        # Stop the processes gracefully
        if self.screenshot_process:
            self.screenshot_process.join(timeout=5)
            if self.screenshot_process.is_alive():
                self.screenshot_process.terminate()

        if self.summary_process:
            self.summary_process.join(timeout=5)
            if self.summary_process.is_alive():
                self.summary_process.terminate()

        self.master.after(100, self.terminate_application)

    def terminate_application(self):
        print("Terminating application...")
        self.master.quit()
        sys.exit(0)

    def on_closing(self):
        self.stop_processes()

def get_file_path():
    current_time = datetime.now()

    # Format the date and time as 'YYYY-MM-DD' for date and 'HH-MM-SS' for time
    date_str = current_time.strftime("%Y-%m-%d")
    time_str = current_time.strftime("%H-%M-%S")

    # Generate the file name in the required format
    filename = f"Answers-{date_str}-{time_str}"

    # Print the generated filename
    return(filename)

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    os.environ['ANSWER_FILE_PATH'] = get_file_path()
    root.mainloop()
