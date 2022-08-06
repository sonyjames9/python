def merge_sort(arr):
  if len(arr) > 1:
    # Split to left and right
    mid = int(len(arr)/2)
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Uncomment to check the formation left and right arrays
    # print(f"Before merge left: {left_half}")
    # print(f"Before merge right: {right_half}")

    # Recursive calls
    merge_sort(left_half)
    merge_sort(right_half)

    # Uncomment to check the formation left and right arrays
    # print(f"After merge left: {left_half}")
    # print(f"After merge right: {right_half}")
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1

      k += 1
    #Uncomment to check the arr
    # print(f"array : {arr}")

    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1

  #Uncomment to check the merge
  # print(f"Merge array : {arr}")
  return arr


arr = [5, 3, 7, 9, 6, 1, 0, 4, 17, 20, 15, 11, 30, 35, 40]
print(
    f"Merge sort array {arr} sorted to : {merge_sort(arr)}")
