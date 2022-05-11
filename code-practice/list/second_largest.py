from os import system
from more_itertools import first


def second_largest(arr):
  arr_size = len(arr)
  if (arr_size < 2):
    print("Invalid input")
    return

  first = second = -2147483648
  for ctr in range(arr_size):

    # if current element is smaller than first,
    # then update both first and second
    if(arr[ctr] > first):
      second = first
      first = arr[ctr]

    # If arr[i] is in between the first and second,
    # then update second
    elif (arr[ctr] > second and arr[ctr] != first):
      second = arr[ctr]
  if (second == -2147483648):
    print("There is no second largest element")
  else:
    print("The second largest element is : ", second)


second_largest([12, 35, 1, 10, 34, 1])
second_largest([16, 15, 36, 35, 1, 10, 34, 1])
