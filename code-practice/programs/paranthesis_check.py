def valid_paranthesis_check(paranthesis_str):
  if len(paranthesis_str) % 2 != 0:
    return False

  opening = set('([{')
  matches = set([('(', ')'), ('[', ']'), ('{', '}')])

  stack = []

  for char in paranthesis_str:
    if char in opening:
      stack.append(char)

    else:
      if len(stack) == 0:
        return False
      last_open = stack.pop()

      if (last_open, char) not in matches:
        return False

  return len(stack) == 0


print(valid_paranthesis_check('((()))'))
print(valid_paranthesis_check('()()()'))
print(valid_paranthesis_check('(())()'))
print(valid_paranthesis_check('()(())'))
