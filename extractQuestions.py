def extract_questions(text):
    # Split the text based on the pattern "Question X:"
    questions = text.split('Question ')
    
    # Remove any empty strings from the list
    questions = [q.strip() for q in questions if q.strip()]

    # Add the "Question " prefix back to the questions
    questions = ['Question ' + q for q in questions]

    return questions

if __name__ == "__main__":
    # Sample text containing questions
    text = """Question 4: Summarize six important properties of relations.
For the toolbar, press ALT+F10 (PC) or ALT+FN+F10 (Mac).

Question 5: What is the evaluation order for the Boolean operators (AND, OR, NOT) in an SQL command? How can a query writer be sure that the operators will work in order? 
For the toolbar, press ALT+F10 (PC) or ALT+FN+F10 (Mac)."""

    # Extract questions
    questions = extract_questions(text)
    
    # Print each question
    for idx, question in enumerate(questions):
        print(f"Question {idx+1}: {question}")
