# # # Given an integer number, N, it has to return the smallest integer
# # # near the integer N, bigger than N, in which the sum of digits is
# # # as big as twice the sum of digits of N.
# # # For example if N is 12 (1+2=3), the algorithm must return 15 (1+5=6).
# # # For example if N is 13 (1+3=4), the algorithm must return 17 (1+7=8).
# # # For example if N is 14 (1+4=5), the algorithm must return 19 (1+9=10).
# # # For example if N is 15 (1+5=6), the algorithm must return 39 (3+9=12).
# # # For example if N is 16 (1+6=7), the algorithm must return 59 (5+9=14).
# # # For example if N is 17 (1+7=8), the algorithm must return 79 (7+9=16).
# # # For example if N is 18 (1+8=9), the algorithm must return 81 (+9=81).
# # # For example if N is 24 (2+4=6), the algorithm must return 39 (3+9=12).
# # # For example if N is 26 (2+6=8), the algorithm must return 79 (7+9=16).

# # from operator import concat


# # def smallest_sum_of_digits_and_twice_as_num(num):
# #   if num < 0:
# #     print("Number needs to be greater than 9")
# #     return "Number needs to be greater than 9"
# #   if num < 10:
# #     print("Number needs to be greater than 9")
# #     return "Number needs to be greater than 9"
# #   sum_of_num = sum_of_digits(num)
# #   print(str(sum_of_num) + " ", end="")
# #   twice_of_sum = 2 * sum_of_num
# #   print(twice_of_sum, end=" ")

# #   bigger_nums = []
# #   for index in range(twice_of_sum):
# #     result = twice_of_sum-index
# #     value = concat(str(result), str(index))
# #     value = int(value)
# #     bigger_nums.append(value)
# #   # return bigger_nums

# #   # for i in bigger_nums:
# #   #   min_value = min(i)
# #   min_value = min(bigger_nums)
# #   print(min_value)
# #   return min_value


# # def sum_of_digits(num):
# #   if num == 0:
# #     return 0
# #   if num == 1:
# #     return 1
# #   res = 0

# #   if num > 0:
# #     return (res + (num % 10)) + sum_of_digits(num//10)

# # # find the smallest integer bigger than N, in which the sum of digits is as big as twice the sum of digits of N


# # smallest_sum_of_digits_and_twice_as_num(-1)
# # smallest_sum_of_digits_and_twice_as_num(2)
# # smallest_sum_of_digits_and_twice_as_num(12)
# # smallest_sum_of_digits_and_twice_as_num(13)
# # smallest_sum_of_digits_and_twice_as_num(14)
# # smallest_sum_of_digits_and_twice_as_num(15)
# # smallest_sum_of_digits_and_twice_as_num(16)
# # smallest_sum_of_digits_and_twice_as_num(17)
# # # print(min(test))
# # smallest_sum_of_digits_and_twice_as_num(18)
# # smallest_sum_of_digits_and_twice_as_num(19)
# # smallest_sum_of_digits_and_twice_as_num(20)
# # smallest_sum_of_digits_and_twice_as_num(21)
# # smallest_sum_of_digits_and_twice_as_num(22)
# # smallest_sum_of_digits_and_twice_as_num(23)
# # smallest_sum_of_digits_and_twice_as_num(24)

# # def solution(time):
# #   hours = int(time[:2])
# #   minutes = int(time[3:])
# #   # print(hours)
# #   # print(minutes)

# #   if ((0 <= hours < 24) and (0 <= minutes < 60)):
# #     return True

# #   return False


# # print(solution("13:58"))
# # print(solution("13:78"))
# # print(solution("33:58"))
# # print(solution("03:58"))
# # print(solution("03:00"))
# # print(solution("00:00"))


# # def solution(digits):
# #   if digits:
# #     str_digits = ""
# #     for i in range(len(digits)):
# #       str_digits += str(digits[i])
# #     str_digits = str(int(str_digits) + 1)
# #     # str_digits += 1
# #     # str_digits = str(str_digits)
# #     # list_of_digits = list(str_digits)
# #     list_of_digits = list(map(int, str_digits))
# #     # list_of_digits = [int(i) for i in list_of_digits]

# #   return list_of_digits


# # print(solution([1, 2, 3, 4]))
# # print(solution([9, 9, 9]))


# from array import array
import random


def solution(inp_array, k):
    pos = random.randint(0, len(inp_array) - 1)
    left = []
    right = []

    for i in range(len(inp_array)):
        if inp_array[i] <= inp_array[pos]:
            left.append(inp_array[i])
        else:
            right.append(inp_array[i])

    if len(left) > 1:
        left = sorted(left, reverse=True)
    if len(right) > 1:
        right = sorted(right, reverse=True)

    print(str(left) + "  " + str(right))

    # if len(left) < 1:
    #     return right[k-1:k]
    # elif len(right) < 1:
    #     return left[k-1:k]
    # else:
    #     return find_k(left, right, k)
    if_left_exists(left, right, k)
    if_right_exists(left, right, k)

    if len(left) > 1 and len(right) > 1:
      return find_k(left, right, k)


def find_k(left, right, k):

  for k in range(k, 0, -1):
    if_left_exists(left, right, k)
    if_right_exists(left, right, k)
    if len(left) < 1:
      return right[k-1:k]
    elif len(right) < 1:
      return left[k-1:k]
    else:
      max_num = max(max(left), max(right))
      if max_num in left:
        left.remove(max_num)
      elif max_num in right:
        right.remove(max_num)

  return max_num


def if_right_exists(left, right, k):
  if len(right) < 1:
    return left[k-1:k]


def if_left_exists(left, right, k):
  if len(left) < 1:
    return right[k-1:k]


print(solution([19, 32, 11, 23], 3))
print(solution([1, 4, 10, 5, 2], 1))
print(solution([19, 32, 11, 23, 13, 10, 9, 12, 14], 3))
print(solution([1, 4, 2, 5, 7, 3, 6], 3))
