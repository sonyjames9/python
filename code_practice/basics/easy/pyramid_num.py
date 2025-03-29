def print_number_pyramid(rows):
  """
  o/p:
      1
    123
    12345
  1234567
  123456789
  """

  for i in range(1, rows + 1):
    # print spaces
    for j in range(rows - i):
      print(" ", end="")
    for j in range(2 * i -1):
      print(j + 1, end="")
    print()

print_number_pyramid(5)


"""
1234
123
12
1

"""
def print_half_number_pyramid(rows):
  for i in range(1, rows + 1):
    for j in range(rows - i):
      print(j+1, end="")
    print()

print_half_number_pyramid(5)