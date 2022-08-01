class StackImpl():
  """
  Last in first out principle

  Stack Implementations ---

  is_empty
  push
  pop
  peek
  size
  """

  def __init__(self) -> None:
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)


stack_obj = StackImpl()
print("Stack length : {}".format(stack_obj.size()))
print("Stack isEmpty : {}".format(stack_obj.is_empty()))
stack_obj.push('a')
stack_obj.push('b')
stack_obj.push('c')

print("Stack length : {}".format(stack_obj.size()))
print("Stack isEmpty : {}".format(stack_obj.is_empty()))
print("Stack peek : {}".format(stack_obj.peek()))
