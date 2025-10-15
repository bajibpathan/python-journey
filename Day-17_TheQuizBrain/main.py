# main.py
# ----------------------------------------------
# Main entry point for the Quiz Brain project.
# This file handles the creation of questions, 
# initializes the quiz engine, and controls the quiz flow.
# ----------------------------------------------

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store all Question objects
question_bank = []

# Loop through each question in the question_data list and convert it into a Question object
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the quiz with the list of questions
quiz = QuizBrain(question_bank)

# Continue asking questions until there are none left
while quiz.still_has_questions():
    quiz.next_question()

# Display final results
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")
