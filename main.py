from question import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for data in question_data:
    newQuestion = Question(data["question"],data["correct_answer"])
    question_bank.append(newQuestion)
    # print(newQuestion.text)

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)
# while quiz.still_has_question():
#     quiz.next_question()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")

