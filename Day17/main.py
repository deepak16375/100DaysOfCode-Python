# Import necessary classes and data for the quiz
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store Question objects
question_bank = []

# Iterate through the provided question data and create Question objects
for question in question_data:
    question_text = question["question"]  # Extract question text
    question_answer = question["correct_answer"]  # Extract correct answer
    new_question = Question(question_text, question_answer)  # Create a Question object
    question_bank.append(new_question)  # Add the Question object to the question_bank list

# Create a QuizBrain object using the question_bank
quiz = QuizBrain(question_bank)

# Continue asking questions until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()  # Ask the next question

# Display a message when the quiz is completed, along with the final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
