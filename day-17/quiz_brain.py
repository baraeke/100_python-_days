class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0  # Initialize question counter
        self.question_list = question_bank  # Store the list of question objects
        self.score = 0 # Initialize score counter

    def next_question(self):
        """Fetches the next question and increments the question number"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)?: ").lower() 
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Returns True if there are still questions available on the question bank otherwise False"""
        if self.question_number < len(self.question_list):
            return True
        else:
            return False 
        
    def check_answer(self, user_answer, correct_answer):
        """Checks if the users option is the right answer and return score"""
        if user_answer == correct_answer:
            print("You are right!")
        else:
            print("Opps you are wrong")
        print(f"The correct answer was {correct_answer}")
        