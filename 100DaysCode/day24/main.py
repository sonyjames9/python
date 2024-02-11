file = open("100DaysCode/day24/wtest.txt")
contents = file.read()
print(contents)
file.close()

# write to file
with open("100DaysCode/day24/test.txt", "w") as file:
  file.write("new contents added to file")
  # contents = file.read()
  # print(contents)

  
# No close required
with open("100DaysCode/day24/test.txt") as file:
  contents = file.read()
  print(contents)

