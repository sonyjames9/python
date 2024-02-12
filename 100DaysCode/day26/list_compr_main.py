nums_str = "9,1,4,5,6,7,8,3"
nums_list = nums_str.split(',')
print(nums_list)
nums = [int(x) for x in nums_list]

print(nums)

res = [num for num in nums if num%2 == 0]
print(res)


with open('100DaysCode/day26/file1.txt') as file1:
  list1 = file1.readlines()

with open('100DaysCode/day26/file2.txt') as file2:
  list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)