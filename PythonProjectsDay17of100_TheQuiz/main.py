from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  newq = Question(question_text, question_answer)
  question_bank.append(newq)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("Congrats! You finished the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
