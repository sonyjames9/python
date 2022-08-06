import math


def shell_sort(arr):
  sub_list_count = int(len(arr)/2)
  # sub_list_count = math.floor(len(arr)/2)
  while sub_list_count > 0:
    for start in range(sub_list_count):

      gap_insertion_sort(arr, start, sub_list_count)
    print(f"After increments of size : {sub_list_count}")
    print(f"The list is : {arr}")

    sub_list_count = int(sub_list_count/2)
    # sub_list_count = math.floor(sub_list_count/2)
  return arr


def gap_insertion_sort(arr, start, gap):
  for i in range(start+gap, len(arr), gap):
    current_value = arr[i]
    position = i

    while position >= gap and arr[position-gap] > current_value:
      arr[position] = arr[position-gap]
      position = position - gap
    arr[position] = current_value
  return arr


arr = [5, 3, 7, 9, 6, 1, 0]
print(
    f"Shell sort array {arr} sorted to : {shell_sort(arr)}")
