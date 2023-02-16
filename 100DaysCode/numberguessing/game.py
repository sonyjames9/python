from os import system
from wsgiref.util import guess_scheme
from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print("You got it, the answer was {answer}".format(answer=answer))


def difficulty_level():
  diff_level = input("Choose a difficulty leve, Type 'easy' or 'hard' : ")
  if diff_level == 'hard':
    return HARD_LEVEL_TURNS
  else:
    return EASY_LEVEL_TURNS


def launch_game():
  system('cls || clear')
  print(logo)
  print('Whats the number, guess between 1 to 100')
  print('Im thinking of number between 1 and 100')
  answer = randint(1, 100)

  turns = difficulty_level()
  guess = 0

  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")
    guess = int(input("Make a guess : "))
    if turns == 0:
      print("You have run out of guesses, you lose, do you want to try again?")
      try_again = input("Type 'yes' to continue : ")
      if try_again == 'yes':
        launch_game()
      else:
        return
    elif guess != answer:
      print("Guess Again")
    turns = check_answer(guess, answer, turns)


launch_game()
