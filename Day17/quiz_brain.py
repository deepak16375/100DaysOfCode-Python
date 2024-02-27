# Define a class named QuizBrain
class QuizBrain:

    # Constructor method to initialize the QuizBrain object with a question list
    def __init__(self, q_list):
        self.question_number = 0  # Initialize the question number
        self.score = 0  # Initialize the score
        self.question_list = q_list  # Store the list of questions

    # Method to check if there are still questions left in the quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Method to present the next question to the user
    def next_question(self):
        current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Move to the next question
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  # Get user's answer
        self.check_answer(user_answer, current_question.answer)  # Check the user's answer

    # Method to check if the user's answer is correct and update the score
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increment the score if the answer is correct
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
