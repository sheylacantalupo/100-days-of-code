from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []  # object list

for q in question_data:  # loop to iterate over question_data
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")