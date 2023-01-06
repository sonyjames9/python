"""
"8199": Palindromes created are
1,8,9,99,919,989
Program should return 989 as largest

You are given string S

39878 should return largest palindrome 898
00900 should return 9
0000 should return 0
54321 should return 5
"""

# count = [0] * 10
# for i in arr:
#   count[int(i)] = count[int(i)] + 1
# i, j = 0, len(count)


def palindrome_list(arr):
  size_of_array = len(arr)
  list_of_nums = [int(num) for num in arr]
  list_of_nums = sorted(list_of_nums, reverse=True)
  print(list_of_nums)
  dict_palindrome = {}
  for num in list_of_nums:
    if num not in dict_palindrome:
      dict_palindrome[num] = 1
    else:
      dict_palindrome[num] += 1

  # for k,v in dict_palindrome:
  #   if dict[num]

  print(dict_palindrome)

  str_val = ""


palindrome_list("8199")
