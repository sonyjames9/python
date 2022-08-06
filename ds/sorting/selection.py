def selection(arr):

  # Indexing reverse manner, largest element will be moved to last slot
  for fill_slot in range(len(arr)-1, 0, -1):
    position_of_max = 0

    # Location is starting at 1 because the position_of_max is at 0.
    # Iterate from lower upto higher range array
    # Looping so that each time a max value is found.
    for location in range(1, fill_slot+1):
      if arr[location] > arr[position_of_max]:
        position_of_max = location

    # This position of max is then swapped at n-1 positions in each iteration
    temp = arr[fill_slot]
    arr[fill_slot] = arr[position_of_max]
    arr[position_of_max] = temp
  return arr


arr = [5, 3, 7, 9, 6, 1, 0]
print(
    f"Selection sort array {arr} sorted to : {selection(arr)}")
