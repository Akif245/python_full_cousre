from question_model import Questions
from data1 import question_data
qb=[]
for question in question_data:
    #question_text=question["text"]
    question_text = question["question"]
    question_answer = question["correct_answer"]
    #question_answer=question["answer"]
    new_ques=Questions(question_text,question_answer)
    qb.append(new_ques)
print(qb)
