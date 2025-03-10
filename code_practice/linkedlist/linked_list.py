from platform import node
from code_practice import arrays

class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return "Node object"


def take_input():
  input_list = [int(elem) for elem in input().split()]
  head = None
  tail = None
  for curr_data in input_list:
    if curr_data == -1:
      break

    new_node = Node(curr_data)
    if head is None:
      head = new_node
      tail = new_node
    else:
      # curr = head
      # while curr.next is not None:
      #   curr = curr.next
      # curr.next = new_node
      tail.next = new_node
      tail = new_node

  return head


def print_linked_list(head):
  while head is not None:
    print(str(head.data) + "->", end='')
    head = head.next

  print("None")
  return


def print_ith_node(head, ith_position):
  ctr = 1
  while head is not None and ctr < ith_position:
    head = head.next
    ctr += 1
  return head.data


def length(head):
  count = 0
  while head is not None:
    head = head.next
    count += 1
  return count


def insert_iterative(head, ith_position, data):
  if ith_position < 0 or ith_position > length(head):
    return head

  ctr = 0
  prev = None
  curr = head
  while ctr < ith_position:
    prev = curr
    curr = curr.next
    ctr += 1

  new_node = Node(data)
  if prev is not None:
    prev.next = new_node
  else:
    head = new_node
    head.next = curr
  new_node.next = curr

  return head


def delete_node(head, position):
  pass


def insert_recursively(head, ith_pos, data):
  if ith_pos < 0:
    return head
  if ith_pos == 0:
    new_node = Node(data)
    new_node.next = head
    return new_node

  if head is None:
    return None

  initial_head = insert_recursively(head.next, ith_pos-1, data)
  head.next = initial_head
  return head

#    else:
#
#
#   pass



head = take_input()

# print_linked_list(head)

# node
# print(f"Value at {print_ith_node(head, 3)}")
# print(f"Value at ith {insert_ith_node(head, 3, 5)}")
print_linked_list(head)
# print(f"Value at ith {insert_ith_node(head, 5, 9)}")
# print_linked_list(head)
insert_recursively(head, 1, 44)
# print(f"Node after insert : {print_linked_list(head)}")
print_linked_list(head)

#
# a = Node(13)
# b = Node(15)
#
# a.next = b
# print(a.data)
# print(b.data)
# print(a.next.data)
# print(a)
# print(a.next)
