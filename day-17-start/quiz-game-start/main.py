from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(key["question"],key["correct_answer"]) for key in question_data]

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")