import random

QUIZ_DATA = [
    {
        "question": "What is the primary data structure used to store ordered, mutable sequences in Python?",
        "options": ["A. Tuple", "B. List", "C. Dictionary", "D. Set"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["A. catch", "B. try", "C. except", "D. handle"],
        "answer": "C"
    },
    {
        "question": "What does the .get() method on a dictionary return if the key is missing by default?",
        "options": ["A. KeyError", "B. 0", "C. None", "D. False"],
        "answer": "C"
    },
    {
        "question": "Which built-in function returns the total number of items in an iterable?",
        "options": ["A. count()", "B. size()", "C. length()", "D. len()"],
        "answer": "D"
    },
    {
        "question": "What is the result of 10 // 3 in Python?",
        "options": ["A. 3.33", "B. 3", "C. 1", "D. 3.0"],
        "answer": "B"
    }
]

def run_quiz():
    questions = QUIZ_DATA.copy()
    random.shuffle(questions)
    score = 0

    total_questions = len(questions)
    for question_number, current_item in enumerate(questions, start=1):
        print(f"\nQuestion {question_number} of {total_questions}:")
        print(current_item["question"])
        
        for option in current_item["options"]:
            print(f"  {option}")
            
        user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if user_answer == current_item["answer"]:
            print("Your answer is correct")
            score += 1
        else:
            print(f"Your answer is wrong. Correct answer: {current_item['answer']}")

    print(f"\nQuiz completed ! You scored {score} out of {total_questions}")

# Entry point to execute the quiz
if __name__ == "__main__":
    run_quiz()