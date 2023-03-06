class QuizBrain():
    def __init__(self, questions_list) -> None:
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        ask_user = input(f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(ask_user, self.questions_list[self.question_number].answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}.")
