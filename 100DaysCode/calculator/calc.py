from audioop import add

from more_itertools import divide
from art import logo
import os


def add(num1, num2):
  return num1 + num2


def subtract(num1, num2):
  return num1 - num2


def multiply(num1, num2):
  return num1 * num2


def divide(num1, num2):
  return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
  print(logo)
  # os.system('cls || clear')
  num1 = float(input("What's the first number ? :"))
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation : ")
    num2 = float(input("What's the next number ? :"))
    calculation_fn = operations[operation_symbol]
    answer = calculation_fn(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    val = input(
        f"Type y to continue calculating with {answer} or type 'r' to restart calculator or type 'n' to exit ")

    if val == "y":
      num1 = answer
    elif val == 'r':
      calculator()
    elif val == 'n':
      print("Thank you")
      should_continue = False


calculator()
