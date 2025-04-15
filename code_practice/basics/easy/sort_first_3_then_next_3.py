nums = [2, 1, 6, 5, 3, 7, 8, 5, 6]
result = []
for i in range(0, len(nums), 3):
    result.extend(sorted(nums[i:i + 3]))
print(result)  # [1, 2, 6, 3, 5, 7, 5, 6, 8]
