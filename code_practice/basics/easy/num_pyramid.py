def print_number_pyramid(rows):
  """
  % /opt/homebrew/bin/python3 /Users/sonyj/Git/sjy/py/py_100_days/python/code_practice/basics/easy/num_pyramid.py
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