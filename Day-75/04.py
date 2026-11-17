# Create a mini quiz engine using dictionaries/lists, score tracking, validation, and functions.


# Mini Quiz Engine

questions = [
    {
        "question": "Which language is used for AI?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "What is the output of 5 + 3?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["if", "for", "break", "continue"],
        "answer": "for"
    },
    {
        "question": "What is the extension of Python files?",
        "options": [".java", ".html", ".py", ".cpp"],
        "answer": ".py"
    }
]


# Function to display questions
def display_question(question, number):

    print("\nQuestion", number)
    print(question["question"])

    for i in range(len(question["options"])):
        print(i + 1, ".", question["options"][i])


# Function to validate answer
def get_answer():

    while True:
        answer = input("Enter your answer (1-4): ")

        if answer in ["1", "2", "3", "4"]:
            return int(answer)

        else:
            print("Invalid input! Please enter between 1 and 4.")


# Function to start quiz
def start_quiz():

    score = 0

    print("\n===== WELCOME TO MINI QUIZ =====")

    for i in range(len(questions)):

        display_question(questions[i], i + 1)

        choice = get_answer()

        selected_answer = questions[i]["options"][choice - 1]

        if selected_answer == questions[i]["answer"]:
            print("Correct Answer!")
            score += 1

        else:
            print("Wrong Answer!")
            print("Correct Answer:", questions[i]["answer"])

    # Final Result
    total = len(questions)
    percentage = (score / total) * 100

    print("\n===== QUIZ RESULT =====")
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print("Final Score:", score, "/", total)
    print("Percentage:", percentage, "%")


# Main Program
start_quiz()