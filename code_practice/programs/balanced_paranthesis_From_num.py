"""
UNIPHORE technologies ------
---------------------
Given a num 6, find all possible ways of valid parenthesis


Result : ((())),()()(),(())(),()(())
"""


def print_parenthesis(str, n):
  if(n > 0):
    _print_parenthesis(str, 0, n, 0, 0)


def _print_parenthesis(str, pos, n, open, close):

  if(close == n):
    for i in str:
      print(i, end="")
    print()

  else:
    if (open > close):
      str[pos] = ')'
      _print_parenthesis(str, pos+1, n, open, close+1)
    if (open < n):
      str[pos] = '('
      _print_parenthesis(str, pos+1, n, open+1, close)


n = 6
str = [""] * 2 * n
# print(str)
# print(len(str))
# print_parenthesis(str, n)


# Python program to print all the combinations of balanced parenthesis.

# function which generates all possible n pairs of balanced parentheses.
# open : count of the number of open parentheses used in generating the current string s.
# close : count of the number of closed parentheses used in generating the current string s.
# s : currently generated string/
# ans : a vector of strings to store all the valid parentheses.
def print_parenthesis_2(n, open, close, s, ans):
  # if the count of both open and close parentheses reaches n, it means we have generated a valid parentheses.
  # So, we add the currently generated string s to the final ans and return.
  if (open == n and close == n):
    ans.append(s)
    return

  # At any index i in the generation of the string s, we can put an open parentheses only if its count until that time is less than n.
  if(open < n):
    print_parenthesis_2(n, open+1, close, s+"(", ans)
  # At any index i in the generation of the string s, we can put a closed parentheses only if its count until that time is less than the count of open parentheses.
  if(close < open):
    print_parenthesis_2(n, open, close+1, s+")", ans)

n = 4
# ans is created to store all the possible valid combinations of the parentheses.
ans = []

print_parenthesis_2(n, 0, 0, "", ans)

# Now, here we print out all the combinations.
for s in ans:
    print(s)
