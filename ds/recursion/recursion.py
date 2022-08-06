# First problem
def reverse_string(string):
    if len(string) == 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


reverse_string("abcde")


# Second problem
""" 
Find all possible permutations from the given string
https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
"""


def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):

                # Just for understanding it better, how permutation is working below, the print statements can be uncommented and checked
                # print('Current letter is: ', let)
                # print('Perm is: ', perm)
                # Add it to output
                out += [let+perm]
    return out


print(permute('abc'))


# Third problem
# Iteration
def fibonacci_iterative(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    return a


print(f"Fibonacci using iteration: {fibonacci_iterative(6)}")


# Recursion
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n

    else:
        return fibonacci_recursive(n-1) + (n-2)


print(f"Fibonacci using recursion: {fibonacci_recursive(7)}")


# Memoization
n = 10
cache = [None] * (n+1)


def fibonacci_dynamic_memoization(n):
  # Base Cache
  if n == 0 or n == 1:
    return n

  # Check Cache
  if cache[n] != None:
    return cache[n]

  # Keep Setting Cache
  cache[n] = fibonacci_dynamic_memoization(
      n-1) + fibonacci_dynamic_memoization(n-2)

  return cache[n]


print(f"Fibonacci using memoization: {fibonacci_dynamic_memoization(10)}")


# https://runestone.academy/ns/books/published/pythonds/Recursion/DynamicProgramming.html
# https://en.wikipedia.org/wiki/Change-making_problem
# Total coins to reach a particular coin value
# https://runestone.academy/ns/books/published/pythonds/_images/callTree.png

# Find the minimum no of coins to return while making a cash txn of a certain amount.
# This approach takes longer for higher value target
def find_coins_recursive(target, coins):
  min_coins = target

  # Base case
  if target in coins:
    return 1
  else:
    # For every coin value thats is <= target value
    # Make a list comprehension for all the coins which is less than target
    for i in [c for c in coins if c <= target]:
      # For each of the coins less than target, subtract coin from target value along with the total coins

      # Add a coin count + recursive
      num_coins = 1 + find_coins_recursive(target-i, coins)

      # If num coins is less than min coins, then reset the min coins
      if num_coins < min_coins:
        min_coins = num_coins

  return min_coins


print(
    f"Finding coins recursively without known results : {find_coins_recursive(15, [1, 5, 10])}")
# print(find_coins_recursive(100, [1, 5, 10, 25])) #Takes longer to execute


def find_coins_recursive_dynamic(target, coins, known_results):
  min_coins = target

  # Base case
  if target in coins:
    known_results[target] = 1
    return 1

  # Return a known result if it happens to be greater than 1
  elif known_results[target] > 0:
    return known_results[target]

  else:
    # For every coin value thats is <= target value
    # Make a list comprehension for all the coins which is less than target
    for i in [c for c in coins if c <= target]:
      # For each of the coins less than target, subtract coin from target value along with the total coins

      # Add a coin count + recursive
      num_coins = 1 + \
          find_coins_recursive_dynamic(target-i, coins, known_results)

      # If num coins is less than min coins, then reset the min coins
      if num_coins < min_coins:
        min_coins = num_coins

        known_results[target] = min_coins

  return min_coins


target = 74
coins = [1, 5, 10, 25]
known_results = [0] * (target+1)
# print(find_coins_recursive_dynamic(15, [1, 5, 10]))
print(
    f"Finding coins recursively using dynamic functions : {find_coins_recursive_dynamic(target, coins, known_results)}")


