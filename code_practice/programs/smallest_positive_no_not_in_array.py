def smallest_positive_no_not_in_array(arr_digits):
  max_value = max(arr_digits)
  if max_value < 0:
    return 1
  set_arr = sorted(set(arr_digits))
  for num in range(1, max_value):
    if num not in set_arr:
      return num
  return max_value + 1

print(smallest_positive_no_not_in_array([-1, -2]))
print(smallest_positive_no_not_in_array([1, 2, 3, -1]))
print(smallest_positive_no_not_in_array([3, 4, -1, 1]))
print(smallest_positive_no_not_in_array([7, 8, 9, 11, 12]))
