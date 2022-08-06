def sequential_search(arr, elem):
  pos = 0
  found = False

  while pos < len(arr) and not found:
    if arr[pos] == elem:
      found = True

    else:
      pos += 1
  return found


def ordered_sequential_search(arr, elem):
  """
  Input array must be ordered/sorted
  """
  arr = sorted(arr)
  pos = 0
  found = False
  stopped = False

  while pos < len(arr) and not found and not stopped:
    if arr[pos] == elem:
      found = True

    else:
      if arr[pos] > elem:
        stopped = True
      else:
        pos += 1
  return found


arr = [2, 5, 7, 3, 8, 4]
element_to_search = 4
print(f"Search element {element_to_search} in array {arr} : {sequential_search(arr, element_to_search)}")
element_to_search = 6
print(f"Search element {element_to_search} in array {arr} : {sequential_search(arr, element_to_search)}")

element_to_search = 6
print(f"Search element {element_to_search} in sorted array {arr} : {ordered_sequential_search(arr, element_to_search)}")
element_to_search = 4
print(f"Search element {element_to_search} in sorted array {arr} : {ordered_sequential_search(arr, element_to_search)}")
