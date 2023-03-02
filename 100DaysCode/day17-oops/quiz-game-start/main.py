from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]

  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

# print(question_bank[1].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

print(f"You have completed the quiz")
print(f"Your final score : {quiz.score}/{quiz.question_num}")

# Sample Questions API : https://opentdb.com/api_config.php
