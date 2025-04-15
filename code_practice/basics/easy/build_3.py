# print("hello" 'world ' * 2)

# class test():
#   id = 0
#   def __init__(self, id) :
#     self.id = id
#     id = 2
# 
# t = test(1)
# print(t. id)

# def a(b,c,d):
#   pass

# a = 7
# print(a.__str__())

# import re
# m = re.search(r'(ab[cd]?)', "acdeabdabcde")
# print(m.groups())

# import datetime
# print(type(datetime.date(2012,1,1,) - datetime.date(2011,1,1)))

# import itertools
# print ([i for i in filter(lambda x: x% 5, itertools.islice(itertools.count(5), 10))])

# import re
# text = "abc123def456ghi"
# pattern  = r"(?:abc)\d+"
# matches = re.findall(pattern, text)
# print(matches)


def Solve(N):
  div = [1]
  for i in range(2, N+1):
    if N % i == 0:
      div.append(i)
      if i!= N // i:
        div.append(N//i)
  print(sum(div))
  if sum(div) == N:
      print(div)
      return "YES"
  else:
    return "NO"

# T = int(input())
# for _ in range(T):
#   N = int(input())
out_ = Solve(3)
print(out_)
out_ = Solve(6)
print(out_)
out_ = Solve(5)
print(out_)
out_ = Solve(28)
print(out_)