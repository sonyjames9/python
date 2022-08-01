# Refer bit_operators.py for understanding bitwise operatots


def find_missing_item(array1, array2):
  res = 0
  for _ in range(len(array1)):
    res = res ^ array1[_]
    # print(res)
  for _ in range(len(array2)):
    res = res ^ array2[_]
  print(res)


find_missing_item([1, 2, 3, 4], [1, 3])
find_missing_item([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])

print("RIGHT : {}".format(20 >> 2))
print(f"Missing item : {find_missing_item([1,2,3,4,5],[1,2,3,4,5,6])}")
