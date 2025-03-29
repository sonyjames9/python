x = 1
y = 2


first = "Sony"
second = "James"

full = f"{first} {second}"
print(full)

string = "abcd"
print("range")
for i in range(len(string)):
  print(string[i], end=" ")

print("\nreverse range")
for i in reversed(range(len(string))):
  print(string[i], end=" ")


# Reverse for loop without using reversed function
print("\nReverse without using reversed keyword")
arr = [1, 2, 3, 4, 5]
# Indexing reverse manner
for n in range(len(arr)-1, 0, -1):
  print(n, end=" ")
