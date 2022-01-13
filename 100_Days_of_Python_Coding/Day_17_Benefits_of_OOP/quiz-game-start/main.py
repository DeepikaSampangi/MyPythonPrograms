from question_model import Question
from data import question_data

question_bank = []
for quest in question_data:
    question_bank.append(Question(text=quest["text"], answer=quest["answer"]))

print(question_bank)
