from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    new_question = Question(text=quest["text"], answer=quest["answer"])
    question_bank.append(new_question)

print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"You final score is {quiz.score}/{quiz.question_number}")
