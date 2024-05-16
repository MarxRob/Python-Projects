# This is the main module of this whole program. This is where the most important functionalities are.
class Quiz:

    def __init__(self, question_data):
        self.questions = question_data
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """Displays the current question as an input to the user, then calls the 'check_answer' method to...
        well, check the answer"""

        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False)?: ")
        self.check_answer(user_answer=user_answer, correct_answer=current_question.answer)

    def still_has_questions(self):
        """Returns 'True' or 'False' depending on whether the user has answered all available questions or not"""
        return self.question_number < len(self.questions)

    def show_score(self):
        """Prints the current score on the screen"""
        print(f"Your score is {self.score}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        """Checks whether the user got the answer right or not.
        For this, both the user answer and the right answer most be provided as arguments. Of course, this is
        no concern of the user, for this function is called inside the 'next_question' function and both arguments
        are automatically given there.
        A visual cue will indicate the result and, if they were in fact correct, the score will be incremented by 1."""

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's right!")
            self.show_score()
        else:
            print("That's wrong!")
            self.show_score()
        print(f"The right answer was: {correct_answer}")
