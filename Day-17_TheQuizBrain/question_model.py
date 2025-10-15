 # quiz_model.py
# ----------------------------------------------
# Defines the Question class used to model each
# question object with its text and correct answer.
# ----------------------------------------------

class Question:
    def __init__(self, q_text, q_answer):
        """Initialize a new question with text and answer."""
        self.text = q_text
        self.answer = q_answer
