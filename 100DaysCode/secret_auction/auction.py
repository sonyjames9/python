from art import logo
import os


def secret_auction():
  bidding_finished = False
  bidder_dict = {}
  while not bidding_finished:
    print(logo)
    bidder_name = input("What is your name ? ")
    bidder_val = int(input("What is your bid value ? $ "))
    bidder_dict[bidder_name] = bidder_val
    continue_bidding = input("Is there more bidders; yes or no ? ")
    if continue_bidding == 'no':
      bidding_finished = True
      find_highest_bidder(bidder_dict)
    elif continue_bidding == 'yes':
      bidding_finished = False
      os.system('cls || clear')


def find_highest_bidder(bidder_dict):
  max_bidder_name = ""
  max_bidder_val = -1
  for bidder_name, bid_value in bidder_dict.items():
    if max_bidder_val < bid_value:
      max_bidder_val = bid_value
      max_bidder_name = bidder_name

  print(
      f"Highest bidder is {max_bidder_name} and value is {max_bidder_val}")


secret_auction()
