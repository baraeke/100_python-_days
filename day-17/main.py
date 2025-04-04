from question_model import Question
from data import question_data
from quiz_brain import QuizBrain




question_bank = []
for items in range(len(question_data)):
    text = question_data[items]["text"]
    answer = question_data[items]["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)  


while quiz_brain.still_has_questions():
    quiz_brain.next_question()