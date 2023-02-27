import random
from re import A
from game_data import data
from art import logo, vs
from os import system

# Display art
print(logo)
score = 0

# Format the account data into printable format


def guess_correct(guess, a_followers, b_followers):
  # Get Follower count of each account
  # Use if statement to check if user is correct
  if account_a['follower_count'] > account_b['follower_count']:
      return guess == 'a'
  else:
    return guess == 'b'


def format_data(account):
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']

  return f" {account_name}, a {account_desc}, from {account_country}"


account_b = random.choice(data)
continue_game = True
# Make the game repeatable
while continue_game:
  # Generate a random account from the game data
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  # Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

  a_followers = account_a['follower_count']
  b_followers = account_b['follower_count']

  # Give user feedback on their guess
  system('cls || clear')
  print(logo)

  is_correct = guess_correct(guess, a_followers, b_followers)
  if is_correct:
    # Score keeping
    score += 1
    print(f"youre right! Current score: {score}")
    continue_game = True
  else:
    print(f"youre wrong. Final score: {score}")
    continue_game = False

  # Making account at position B become the next account at position A

  # Clear screen in each round
