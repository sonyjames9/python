"""
list = [1, 3, 6, 4, 1, 2]
Greatest num : 6
Smallest num : 1
"""
# find the greatest number
def find_greatest_num(num_list):
  greatest_num = num_list[0]
  for num in num_list:
    if num > greatest_num:
      greatest_num = num
 
  return greatest_num

print(f"Greatest num : {find_greatest_num ([1, 3, 6, 4, 1, 2])}")

def find_smallest_num(num_list):
  # num_list.sort()
  smallest_num = num_list[0]
  for num in num_list:
    if num < smallest_num:
      smallest_num = num
  return smallest_num

print(f"Smallest num : {find_smallest_num ([1, 3, 6, 4, 1, 2])}")
