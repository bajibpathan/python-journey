# quiz_brain.py
# ----------------------------------------------
# Contains the QuizBrain class which manages the quiz logic.
# Responsible for asking questions, checking answers,
# tracking scores, and determining quiz progress.
# ----------------------------------------------

class QuizBrain:
    def __init__(self, q_list):
        """Initialize with a list of questions and reset counters."""
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Check if there are any remaining questions in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Ask the next question and get user input."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Validate the user's answer and update the score."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✅ You got it right!")
        else:
            print("❌ That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")
