# Online Quiz System

# Function to conduct the quiz
def conduct_quiz(questions, options, answers):
    score = 0

    for i in range(len(questions)):
        print("\nQuestion", i + 1, ":", questions[i])

        for option in options[i]:
            print(option)

        try:
            choice = input("Enter your answer (A/B/C/D): ").strip().upper()

            if choice not in ["A", "B", "C", "D"]:
                print("Invalid option! No marks awarded.")
            elif choice == answers[i]:
                print("Correct Answer!")
                score += 1
            else:
                print("Wrong Answer!")
                print("Correct answer is:", answers[i])

        except Exception as error:
            print("An error occurred:", error)

    return score


# Function to display the final result
def display_result(score, total):
    print("\n--- QUIZ RESULT ---")
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print("Final Score:", score, "/", total)

    percentage = (score / total) * 100
    print("Percentage:", round(percentage, 2), "%")


# Main program
questions = [
    "Which language is used for Python programming?",
    "Which keyword defines a function in Python?",
    "Which data type stores multiple values in a single variable?",
    "Which symbol is used for comments in Python?"
]

options = [
    ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
    ["A. function", "B. define", "C. def", "D. fun"],
    ["A. Integer", "B. Float", "C. Boolean", "D. List"],
    ["A. #", "B. @", "C. $", "D. &"]
]

answers = ["B", "C", "D", "A"]


def main():
    print("===== ONLINE QUIZ SYSTEM =====")
    print("Answer the following multiple-choice questions.")

    score = conduct_quiz(questions, options, answers)
    display_result(score, len(questions))


# Start the quiz
main()