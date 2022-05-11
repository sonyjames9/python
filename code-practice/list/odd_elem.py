def find_odd(l):
  res = 0
  for x in l:
    res = res ^ x
  return res
print(find_odd([15,9,9,20,15,20,6]))