def insertion(arr):

  for ctr in range(1, len(arr)):
    current_val = arr[ctr]
    position = ctr

    while position > 0 and arr[position - 1] > current_val:
      arr[position] = arr[position - 1]
      position = position - 1
    arr[position] = current_val
  return arr


arr = [5, 3, 7, 9, 6, 1, 0]
print(
    f"Insertion sort array {arr} is sorted to : {insertion(arr)}")

# Ref: https://en.wikipedia.org/wiki/Insertion_sort
