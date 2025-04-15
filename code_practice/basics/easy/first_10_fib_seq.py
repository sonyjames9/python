# n = 10
"""
fibonacci
Enter the max sequence : 11
o/p: 
0 1 1 2 3 5 8 13 21 34 55
"""
n = int(input("Enter the max sequence : "))
cnt = 1
a,b = 0,1
while cnt <= n:
  print(a, end=" ")
  cnt += 1
  a,b = b,a
  b = a+b


print("\n\nFibo range 10")


def fibonacci(n):
  a, b = 0, 1
  for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

fibonacci(10)  # 0 1 1 2 3 5 8 13 21 34
