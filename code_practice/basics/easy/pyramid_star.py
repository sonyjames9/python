"""
o/p:
    *
   ***
  *****
 *******
*********
"""
def print_half_number_pyramid(rows):
  for i in range(1, rows + 1):
    # print spaces
    for j in range(rows - i):
      print(" ", end="")
    for _ in range(2 * i -1):
      print("*", end="")
    print()

print_half_number_pyramid(5)

print()


"""
o/p:
*
**
***
****
*****
"""
def print_half_number_pyramid(rows):
  for i in range(1, rows + 1):
    for _ in range(i):
      print("*", end="")
    print()

print_half_number_pyramid(5)