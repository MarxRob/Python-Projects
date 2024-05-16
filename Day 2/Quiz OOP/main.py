# Here is just standard imports, focusing on importing only what's actually going to be used in the program to avoid
# slowing down the code by the loading of stuff that's not applicable to this code.
from question_model import Question
from data import question_data
from quiz_brain import Quiz

# Initialization of the questions used through object creation.
question_bank = []

for item in question_data:

    # In summary, each 'question' in this loop will be created based on the 'Question' class, which in turn need both
    # a question text and an answer as arguments. These two will be provided in the 'for loop' as each item,
    # which represents every element in the 'question_data'.
    question = Question(q_text=item['text'], q_answer=item['answer'])
    question_bank.append(question)

# Object created based on the 'Quiz' class.
quiz_instance = Quiz(question_bank)

# Loop that will keep running while there's still questions. This condition is checked by a function of the
# 'quiz_instance' object that returns 'True' or 'False' depending on whether the user have answered every question
# or not.
while quiz_instance.still_has_questions():
    answer = quiz_instance.next_question()

# Simple display of the final results.
print(f"You have completed the quiz!")
print(f"Your score was {quiz_instance.score}/{quiz_instance.question_number}")
