class Node():
  def __init__(self, value, next=None) -> None:
    self.value = value
    self.next = next

  def get_next(self):
    return self.next


class Singly(Node):
  def __init__(self, head=None) -> None:
    self.head = head
    self.size = 0

  def get_size(self):
    return self.size

  def add(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

  def next_node(self, value):
    node = Node(value, self.head)
    node.next = self.head
    self.head = node
    self.size += 1

  def print_nodes(self):
    current = self.head
    while current:
      print(current.value, end="")
      current = current.next
      if current:
        print(end="->")
    print()

  def check_circular(self):
    slow_ptr = self.head
    fast_ptr = self.head

    while slow_ptr != None and fast_ptr.next != None:
      slow_ptr = slow_ptr.next
      fast_ptr = fast_ptr.next.next

      if slow_ptr == fast_ptr:
        return True

    return False


linked_list = Singly()
# linked_list.add(1)
# linked_list.add(2)
# linked_list.add(3)
# linked_list.print_nodes()
a = Singly(1)
b = Singly(2)
c = Singly(3)

a.next_node = b
b.next_node = c
c.next_node = a

a.check_circular()
