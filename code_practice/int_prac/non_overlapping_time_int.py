def merge_intervals(intervals):
  if not intervals:
    return []
  
  intervals.sort(key=lambda x: x[0])
  initial_list = [intervals[0]]

  for next_list in intervals[1:]:
    last_elem_initial_list = initial_list[-1][1]
    # print(last_elem_initial_list)
    if next_list[0] <= last_elem_initial_list <= next_list[1]:
      initial_list[0][1] = next_list[1]
    else:
      initial_list.append(next_list)
  
  return initial_list


print(merge_intervals([[1,3], [2, 6], [8, 10], [11,12]]))
print(merge_intervals([[1,2], [3, 7], [7, 10], [11,12]]))
print(merge_intervals([[1,2], [2, 9], [8, 10], [11,12]]))
print(merge_intervals([[1,2], [2, 9], [8, 11], [11,12], [15, 17]]))
print(merge_intervals([[1,2], [3, 4], [8, 10], [11,12]]))
