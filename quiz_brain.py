class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Returns True if there are still questions left, otherwise returns False."""
        return self.question_number < len(self.questions_list)

    def next_question(self):
        """Gets the current question, increments question number, asks for and checks user answer."""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f' Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)
        if self.question_number == len(self.questions_list):
            print("You've completed the quiz.")
            print(f"Your final score was: {self.score}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        """Increments user score if user answered the question correctly
        and prints answer + score after every question."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")




