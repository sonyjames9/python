class Node():
  """
  Create a base class Node which will create a node with value and pointer to next. During init it will be None
  """

  def __init__(self, value, next=None) -> None:
    self.value = value
    self.next = next

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next

  def set_next(self, value):
    self.value = value


class Singly(Node):

  """
  """

  def __init__(self, head=None) -> None:
    self.head = head
    self.size = 0

  def get_size(self):
    return self.size

  def add(self, value):
    node = Node(value, self.head)
    node.next = self.head
    self.head = node
    self.size += 1

  def print_nodes(self):
    current = self.head
    while current:
      print(current.get_value(), end="")
      current = current.get_next()
      if current:
        print(end="->")
    print()

  def reverse(self):
    prev = None
    current = self.head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev


  def recursive_call(self, curr, prev):

    # If last node mark it head
    if curr.next is None:
      self.head = curr

      # Update next to prev node
      curr.next = prev
      return

    # Save curr.next node for recursive call
    next_node = curr.next

    # And update next
    curr.next = prev

    self.recursive_call(next_node, curr)

  # recursive_call(test, curr, prev)

  def reverse_recursive(self):
    if self.head is None:
      return
    recursive_call(self.head, prev)


linked_list = Singly()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.print_nodes()
linked_list.reverse()
linked_list.print_nodes()
# linked_list.reverse_recursive()
# linked_list.print_nodes()
