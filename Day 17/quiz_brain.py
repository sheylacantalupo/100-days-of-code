class QuizBrain:
    def __init__(self, q_list):  # question_data
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):  # method
        q_current = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {q_current.text} (True/False):")
        self.check_answer(user_answer, q_current.answer)

    def still_has_questions(self):
        questions = len(self.question_list)   # number of questions the list has
        while self.question_number != questions:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")