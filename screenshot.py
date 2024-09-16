import tkinter as tk
from PIL import ImageGrab
import os
from datetime import datetime

SAVE_FOLDER = "D:\Projects\EasyAssignments\screenshots"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Tool")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.5)  # Transparency for the app window
        self.root.attributes("-topmost", True)
        
        self.canvas = tk.Canvas(self.root, cursor="cross", bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Displaying instructions on the screen
        self.text = self.canvas.create_text(
            self.root.winfo_screenwidth() // 2,
            50,
            text="Draw an area to capture a screenshot",
            fill="white",
            font=("Arial", 24)
        )

        self.start_x = None
        self.start_y = None
        self.rect = None
        self.screenshot_callback = None  # For the callback

        # Binding mouse and keyboard events
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.root.bind("<space>", self.reset_canvas)
        self.root.bind("<Escape>", self.exit_app)

    def set_screenshot_callback(self, callback):
        """Registers a callback to be called when a screenshot is taken."""
        self.screenshot_callback = callback

    def on_press(self, event):
        """Event when the mouse button is pressed to start selecting an area."""
        self.start_x = event.x
        self.start_y = event.y
        self.root.attributes("-alpha", 0.01)  # Lower transparency when selecting
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)

    def on_drag(self, event):
        """Event for dragging the mouse to select the screenshot area."""
        cur_x, cur_y = event.x, event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        """Event when the mouse button is released to finalize the area selection."""
        end_x, end_y = event.x, event.y
        self.root.attributes("-alpha", 0.5)  # Restore transparency after selection
        self.capture_screenshot(self.start_x, self.start_y, end_x, end_y)
        self.canvas.delete(self.rect)  # Reset the rectangle after the screenshot

    def capture_screenshot(self, x1, y1, x2, y2):
        """Captures a screenshot for the selected area and saves it with a timestamp."""
        if x1 != x2 and y1 != y2:  # Ensure valid area is selected
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            screenshot = ImageGrab.grab(bbox=(x1+50, y1, x2+240, y2+220))

            # Generating filename with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"Screenshot_{timestamp}.png"
            file_path = os.path.join(SAVE_FOLDER, filename)

            screenshot.save(file_path)
            print(f"Screenshot saved at {file_path}")

            # If a callback is set, call it with the screenshot path
            if self.screenshot_callback:
                self.screenshot_callback(file_path)

            # Display the prompt for user to continue or exit
            self.show_prompt()

    def show_prompt(self):
        """Displays a message asking the user to continue or exit."""
        self.prompt_text = self.canvas.create_text(
            self.root.winfo_screenwidth() // 2,
            self.root.winfo_screenheight() // 2,
            text="Screenshot saved! Press Space to take another or Esc to exit.",
            fill="white",
            font=("Arial", 20)
        )

    def reset_canvas(self, event):
        """Resets the canvas by removing the prompt and allowing the user to take another screenshot."""
        if hasattr(self, 'prompt_text'):
            self.canvas.delete(self.prompt_text)

    def exit_app(self, event):
        """Exit the application."""
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
