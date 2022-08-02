def largest_cont_sum(array):
  max_so_far = array[0]
  curr_max = array[0]
  for i in range(0, len(array)):
    curr_max = max(array[i], curr_max + array[i])
    max_so_far = max(max_so_far, curr_max)

  return max_so_far


print(
    f"largest cont sum: {largest_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])}")
print(
    f"largest cont sum: {largest_cont_sum([-1, -2, -1, -3, -4, -10, 10, -10, -1])}")
print(f"largest cont sum: {largest_cont_sum([-2,1,-3,4,-1,2,1,-5,4])}")
