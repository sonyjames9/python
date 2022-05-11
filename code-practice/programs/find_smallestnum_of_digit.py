# Print the smallest number of the value and the number of digits
# N = 10, d=2, op= 19
# N = 9,  d=2, op= 18
# N = 20, d=3, op= 299
# N = 20, d=2, op=


num = 9
digits = 2


def find_smallest_num(num, digits):

  # if sum of digits is 0, then smallest number can be
  # generated only if number of digits is 1
  n = num
  if (num == 0):
    if (digits == 0):
      print("Smallest number is 0")
    else:
      print("Not possible")
    return

  # If num greater than 9*digits, then do nothing

  if(num > 9*digits):
    print("Not possible")
    return

  # create an array to store the digits
  res_arr = [0 for i in range(digits+1)]

  # deduct sum by one for the condition where "1" is available for left most digit.
  num -= 1

  # Fill last digits -1 (from: right to left)
  for i in range(digits-1, 0, -1):
    # Each time if num is greater than 9, then digits from right to left will be 9
    if (num > 9):
      # Numbers will be stored first in units, tens, hundreds, thousand and so on.
      res_arr[i] = 9
      num -= 9
    else:
      res_arr[i] = num
      num = 0

  # The last digit to extreme left will be stored here, also 1 was subtracted.
  # That should be added here
  res_arr[0] = num + 1

  print(f"Smallest number of {n} and digits {digits} is ", end="")

  for i in range(digits):
    print(res_arr[i], end="")
  print()


find_smallest_num(10, 2)
find_smallest_num(15, 2)
find_smallest_num(20, 3)
# find_smallest_num(2, 10)
# find_smallest_num(2, 10)
# find_smallest_num(2, 10)
