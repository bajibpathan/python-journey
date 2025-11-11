import html

class QuizBrain:
    """
    Handles all quiz-related logic:
    - Managing questions and current score
    - Verifying answers
    - Tracking progress
    """

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Return True if there are remaining questions in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Fetch the next question from the list, unescape HTML entities
        (e.g., &quot; → "), and return it as a formatted string.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        """
        Check if the user's answer matches the correct one.
        Increase score if correct and return True/False for feedback.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
