def binary_search(arr, search_element):
  first = 0
  last = len(arr) - 1

  found = False

  while first <= last and not found:
    mid = int((first+last)/2)

    if arr[mid] == search_element:
      found = True
    elif search_element < arr[mid]:
      last = mid - 1
    else:
      first = mid + 1

  return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element_to_search = 8
print(
    f"Binary Search element {element_to_search} in array {arr} : {binary_search(arr, element_to_search)}")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
element_to_search = 11
print(
    f"Binary Search element {element_to_search} in array {arr} : {binary_search(arr, element_to_search)}")


def recursive_binary_search(arr, search_element):
  if len(arr) == 0:
    return False
  else:
    mid = int(len(arr)/2)

    if arr[mid] == search_element:
      return True
    elif element_to_search < arr[mid]:
      return recursive_binary_search(arr[:mid], element_to_search)
    else:
      return recursive_binary_search(arr[mid+1:], element_to_search)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element_to_search = 8
print(
    f"Recursive binary Search element {element_to_search} in array {arr} : {recursive_binary_search(arr, element_to_search)}")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
element_to_search = 11
print(
    f"Recrusive binary Search element {element_to_search} in array {arr} : {recursive_binary_search(arr, element_to_search)}")
