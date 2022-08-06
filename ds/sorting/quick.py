def quick_sort(arr):

  quick_sort_helper(arr, 0, len(arr)-1)
  return arr


def quick_sort_helper(arr, first, last):
  if first < last:

    # pivot value assists in splitting
    split_point = partition(arr, first, last)

    quick_sort_helper(arr, first, split_point-1)
    quick_sort_helper(arr, split_point + 1, last)


def partition(arr, first, last):

  # Select pivot value
  pivot_val = arr[first]
  
  left_mark = first+1
  right_mark = last

  done = False

  while not done:

    # The goal of the partition process is to move items from wrong side of pivot value to the correct side
    while left_mark <= right_mark and arr[left_mark] <= pivot_val:

      left_mark += 1

    while right_mark >= left_mark and arr[right_mark] >= pivot_val:
      right_mark -= 1

    # This is where the right and left pointers converge
    if right_mark < left_mark:
      done = True
    
    else:
      temp = arr[left_mark]
      arr[left_mark] = arr[right_mark]
      arr[right_mark] = temp

  temp = arr[first]
  arr[first] = arr[right_mark]
  arr[right_mark] = temp

  return right_mark


arr = [5, 3, 7, 9, 6, 1, 0, 4, 17, 20, 15, 11]
print(
    f"Quick sort array {arr} sorted to : {quick_sort(arr)}")
