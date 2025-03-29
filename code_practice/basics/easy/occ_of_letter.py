"""
/opt/homebrew/bin/python3 /Users/sonyj/Git/sjy/py/py_100_days/python/code_practice/basics/easy/occ_of_letter.py

o/p:
{'l': 1, 'e': 3, 't': 4, 'r': 1, ' ': 1, 's': 1}
"""
str = "letter test"
count = 0
result  = {}

for i in str:
  if i in result:
    result[i] += 1
  else:
    result[i] = 1
print(result)