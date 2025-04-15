def Solve(N):
  if N < 0:
    return "NO"
  
  div_sum = 0
  for i in range(1,N):
    if N % i == 0:
      div_sum += i
  if div_sum == N:
    return "YES"
  else:
    return "NO"
  # # div = [1]
  # div = []
  # for i in range(1, N):
  #   if N % i == 0:
  #     div.append(i)
  #     if i!= N // i:
  #       div.append(N//i)
  # print(div)
  # print(sum(div))
  # if sum(div) == N:
  #     print(div)
  #     return "YES"
  # else:
  #   return "NO"

# T = int(input())
# for _ in range(T):
#   N = int(input())
out_ = Solve(3)
print(out_)
# out_ = Solve(6)
# print(out_)
# out_ = Solve(5)
# print(out_)
out_ = Solve(28)
print(out_)


