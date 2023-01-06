def reverse_list(l):
  s = 0
  e = len(l) - 1
  while s < e:
    l[s], l[e] = l[e], l[s]
    s = s+1
    e = e-1
  return l


print(reverse_list([2, 6, 7, 10, 12, 14, 17, 20]))
