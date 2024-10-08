# Easy Assignment - AI Tool for Effortlessly Solving Your Assignments

**Easy Assignment** is an AI-powered tool designed to help you complete your assignments with minimal effort. Simply take screenshots of your questions, and the tool will generate answers for you using the powerful Gemini API. It's simple, efficient, and saves you time!

## Key Features

- **User-Friendly Interface**: The tool is designed to be intuitive, making it easy for anyone to use.
- **Screenshot Functionality**: Take a screenshot of your questions, and the tool will handle the rest.
- **Batch Processing**: You can upload multiple screenshots at once, and the tool will save all generated answers in a single file.
- **Content Generation**: The tool uses the Gemini API, a cutting-edge AI, to generate answers to your questions.
- **Cross-Platform Support**: Easy Assignment works seamlessly on Windows, macOS(Not Tested), and Linux(Not Working)

## Installation Guide

Follow these steps to set up Easy Assignment on your system, depending on your operating system.

### For Windows

1. **Clone the Repository**  
   First, open Command Prompt and clone the repository using the following command:

   ```bash
   git clone https://github.com/gvarshithreddy/EasyAssignment.git
   ```

2. **Navigate to the Directory**  
   Change to the project directory:

   ```bash
   cd EasyAssignment
   ```

3. **Install Dependencies**  
   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Get your Gemini API Key**  
   Visit [Gemini API Key](https://aistudio.google.com/app/apikey?_gl=1*18mmhy7*_ga*NzQzMzQ4MjYzLjE3MjYyOTM5NjM.*_ga_P1DBVKWT6V*MTcyNjQ3MzMxOS43LjAuMTcyNjQ3MzMxOS42MC4wLjEwMzYwNDY4NTU) to get your API key.

5. **Set up Environment Variables**  
   Create a `.env` file in the project root directory and add the following:

   ```bash
   API_KEY=YOUR_API_KEY
   ANSWER_SAVE_FOLDER=LOCAL_PATH_TO_FOLDER
   ```

6. **Run the Application**  
   Start the application:
   ```bash
   python listener.py
   ```

### For macOS (Don't)

1. **Clone the Repository**  
   Open Terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/gvarshithreddy/EasyAssignment.git
   ```

2. **Navigate to the Directory**  
   Change into the project directory:

   ```bash
   cd EasyAssignment
   ```

3. **Install Dependencies**  
   Use `pip` to install all the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Get your Gemini API Key**  
   Visit [Gemini API Key](https://aistudio.google.com/app/apikey?_gl=1*18mmhy7*_ga*NzQzMzQ4MjYzLjE3MjYyOTM5NjM.*_ga_P1DBVKWT6V*MTcyNjQ3MzMxOS43LjAuMTcyNjQ3MzMxOS42MC4wLjEwMzYwNDY4NTU) to get your API key.

5. **Set up Environment Variables**  
   Create a `.env` file in the project root directory and add the following:

   ```bash
   API_KEY=YOUR_API_KEY
   ANSWER_SAVE_FOLDER=LOCAL_PATH_TO_FOLDER
   ```

6. **Run the Application**  
   Start the application by running:
   ```bash
   python listener.py
   ```

### For Linux (Don't)

1. **Clone the Repository**  
   Open your terminal and clone the repository using:

   ```bash
   git clone https://github.com/gvarshithreddy/EasyAssignment.git
   ```

2. **Navigate to the Directory**  
   Change to the cloned directory:

   ```bash
   cd EasyAssignment
   ```

3. **Install Dependencies**  
   Install the necessary Python dependencies:

   ```bash
   pip3 install -r requirements.txt
   sudo apt-get install python3-tk
   ```

4. **Get your Gemini API Key**  
   Visit [Gemini API Key](https://aistudio.google.com/app/apikey?_gl=1*18mmhy7*_ga*NzQzMzQ4MjYzLjE3MjYyOTM5NjM.*_ga_P1DBVKWT6V*MTcyNjQ3MzMxOS43LjAuMTcyNjQ3MzMxOS42MC4wLjEwMzYwNDY4NTU) to get your API key.

5. **Set up Environment Variables**  
   Create a `.env` file in the project root directory and add the following:

   ```bash
   API_KEY=YOUR_API_KEY
   ANSWER_SAVE_FOLDER=LOCAL_PATH_TO_FOLDER
   ```

6. **Run the Application**  
   Launch the application with:
   ```bash
   python3 listener.py
   ```

## How It Works

Once the app is running, you can:

- **Click on Start to Start the Screenshot tool**
- **Take the screenshot of your questions, make sure the questions are clear**
- **Take a Screenshot**: Capture the questions you want answered. The app will automatically process the screenshot and use the Gemini API to generate responses.
- **Batch Processing**: If you have multiple screenshots, you can take them in succession. All answers will be compiled and saved into a single file, making it easy for you to review later.
- **Open the docx**: The docx is created in the same folder.

## You're All Set!

Now that you've successfully set up Easy Assignment, you can start using the app to make your assignment-solving process faster and easier.
