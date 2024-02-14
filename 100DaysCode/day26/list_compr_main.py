from random import random


nums_str = "9,1,4,5,6,7,8,3"
nums_list = nums_str.split(',')
print(nums_list)
nums = [int(x) for x in nums_list]

print(nums)

res = [num for num in nums if num%2 == 0]
print(res)


with open('100DaysCode/day26/file1.txt') as file1:
  list1 = file1.readlines()

with open('100DaysCode/day26/file2.txt') as file2:
  list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)


# sample list comprehension
# password_letters = [new_item for item in list]
# replaced list comprehension
password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols= [random.choice(symbols) for _ in range(nr_symbols)]
password_numbers= [random.choice(numbers) for _ in range(nr_numbers)]