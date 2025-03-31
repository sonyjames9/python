def build_seq(str):
  for i in range(len(str)):
    print(str[i:] + str[:i])

# build_seq('abbaa')



# write funtion to return how many times first and last letter is same after changing
# sequence of characters in string
def count_same_first_last_char(str):
  count = 0
  for _ in str:
    if str[0] == str[-1]:
      count += 1
  print(count)

# count_same_first_last_char('abbaaccddaa')



# check if string is made of onlye 'a' and/or 'b'
def check_string(str):
  for i in str:
    if i != 'a' or i != 'b':
      print("NO")
    return
  print("YES")

# check_string('abbaaccddaa')



# sort elements in list without using sort function
def sort_list(num_list):
  for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
      if num_list[i] > num_list[j]:
        temp = num_list[i]
        num_list[i] = num_list[j]
        num_list[j] = temp
  print(num_list)

# sort_list([3, 2, 1, 4, 5])


# program to find prime numbers in a given range
def find_prime_numbers(limit):
  for is_prime in range(2, limit):
    status = True
    for divisor in range(2, is_prime):
      if is_prime % divisor == 0:
        status = False
    if status:
      print(is_prime, end=", ")

limit = 10
print(f"List of primes in range {limit}")
find_prime_numbers(limit)


def find_factorial(num):
  fact = 1
  for i in range(1, num+1):
    fact = fact * i
  return fact
print("\nFactorial of 6 is : ", find_factorial(6))


def factorial(n):
  if n == 0:
    return 1 
  return n * factorial(n-1)
print("Factorial of 5 is : ", factorial(5))