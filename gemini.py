import google.generativeai as genai
import os
import PIL
from markdown import markdown
import time
from extractQuestions import extract_questions
from convert import convert_md_to_docx
from dotenv import load_dotenv
load_dotenv('.env')
print(os.getenv("API_KEY"))
genai.configure(api_key=os.getenv("API_KEY"))
generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1,
    )
from datetime import datetime



def append_to_file(file_path, content):
    """
    Appends the specified content to a file.

    :param file_path: The path to the file.
    :param content: The content to append to the file.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(content + '\n')  # Adding a newline character after the content
        print(f"Content successfully appended to {file_path}.")
    except IOError as e:
        print(f"An error occurred while accessing the file: {e}")

ANSWER_SAVE_PATH = os.getenv("ANSWER_SAVE_FOLDER")

def generate_summary(img_path,file_path,length=500,):
    model = genai.GenerativeModel("gemini-1.5-flash")
    time.sleep(1)
    image = PIL.Image.open(img_path)
    questionsPrompt = "There are two questions in the image. What are they?  format outpus as Question#no: The exact content of the question "
    questionsResponse = model.generate_content([questionsPrompt, image])
    questions = extract_questions(questionsResponse.text)
    print(questions)
    answer = ''
    for question in questions:
        print("Writing answer for question: ",question)
        prompt = f"Write a {length} essay to the following question by referencing 'Modern Database Management' by Jeff Hopper, 12th edition (2016). Ensure that your response is precise and clearly linked to the textbook content. Only give the answer, don't say anythong else. \nQuestion: {question}"
        response = model.generate_content(prompt)
        answer+=question+ '\n'+markdown('>'+response.text) + '\n'
    filepath = ANSWER_SAVE_PATH+file_path
    append_to_file(filepath+".md",answer)
    convert_md_to_docx(filepath+".md",filepath+".docx")
    return answer


    

# Example usage
if __name__ == '__main__':
    description = generate_summary(f"D:\\Projects\\EasyAssignments\\screenshots\\Screenshot_2024-09-15_17-13-14.png")
    print(description)