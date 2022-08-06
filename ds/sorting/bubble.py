def bubble_sort(arr):
  for n in range(len(arr)-1, 0, -1):
    # Reduce the loop of n once the greatest num is sorted to the right
    for k in range(n):
      if arr[k] > arr[k+1]:
        temp = arr[k]
        arr[k] = arr[k+1]
        arr[k+1] = temp

  return arr


arr = [5, 3, 7, 9, 6, 1, 0]
print(
    f"Bubble sort array {arr} sorted to : {bubble_sort(arr)}")
