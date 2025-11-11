from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# ---------------------------- BUILDING QUESTION BANK ---------------------------- #
# Create a list of Question objects from the API data.
# Each question consists of a text prompt and the correct answer (True/False).
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# ---------------------------- INITIALIZE QUIZ LOGIC & UI ---------------------------- #
# QuizBrain handles quiz logic (questions, score, etc.)
# QuizInterface builds and controls the Tkinter GUI for user interaction.
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
