def merge_intervals(intervals):
  if not intervals:
    return []
  
  # Sort intervals by start time
  intervals.sort(key=lambda x: x[0])
  result = [intervals[0]]

  for current in intervals[1:]:
      prev = result[-1]
      # print(prev[1])
      # print(current[0])
      # print(current[1])
      if current[0] <= prev[1]:  # Overlap
          prev[1] = max(prev[1], current[1])
      else:
          result.append(current)

  return result

print(merge_intervals([[1,3], [2, 6], [8, 10], [11,12]]))
print(merge_intervals([[1,2], [3, 7], [7, 10], [11,12]]))
print(merge_intervals([[1,2], [2, 3], [4, 6], [5,8], [11,12]]))
print(merge_intervals([[1,2], [2, 9], [8, 11], [11,12], [15, 17]]))
print(merge_intervals([[1,2], [3, 4], [8, 10], [11,12]]))
