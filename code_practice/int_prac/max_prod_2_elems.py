def max_product(list_of_nums):
  if len(list_of_nums) < 2:
    return 0
   
  max1 = max2 = float('-inf')
  min1 = min2 = float('inf')
  # max1 = max2 = -99999
  # min1 = min2 = 999999
  
  for num in list_of_nums:
    if num > max1:
      max2, max1 = max1, num

    elif num > max2:
      max2 = num

    if num < min1:
      min2, min1 = min1, num
    elif num < min2:
      min2 = num

  return max(max1 *  max2, min1 * min2)


print(max_product([-4, -10, 1, 2, 3, 4]))


def max_product2(list_of_nums):
  if len(list_of_nums) < 2:
    return 0

  products = []
  for i in range(len(list_of_nums)):
    for j in range(i):
      product = list_of_nums[i] * list_of_nums[j]
      products.append(product)

  return (max(products))


print(max_product2([-5, -10, 1, 2, 3, 4]))
