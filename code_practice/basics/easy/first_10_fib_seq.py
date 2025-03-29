# n = 10
"""
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