# r- root node as argument
def binary_tree(r):
  return [r, [], []]


def insert_left(root, new_branch):
  # pop out root index at 1, left branch
  t = root.pop(1)

  # If len is greater than 1, means there is some nodes
  if len(t) > 1:
    # If there is already a list, then we insert the new branch with one list
    root.insert(1, [new_branch, t, []])
  else:
    # insert is a method on list with 2 empty lists
    root.insert(1, [new_branch, [], []])
  return root


def insert_right(root, new_branch):
  # pop out root index at 2, right branch
  t = root.pop(2)

  # If len is greater than 1, means there is some nodes
  if len(t) > 1:
    # If there is already a list, then we insert the new branch with one list
    root.insert(1, [new_branch, [], t])
  else:
    # insert is a method on list with 2 empty lists
    root.insert(1, [new_branch, [], []])
  return root


def get_root_val(root):
  return root[0]


def set_root_val(root, new_val):
  root[0] = new_val


def get_left_child(root):
  return root[1]


def get_right_child(root):
  return root[2]


r = binary_tree(3)

insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)

left = get_left_child(r)
print(f" Left node : {left}")
right = get_right_child(r)
print(f" Right node : {right}")

set_root_val(left, 10)
print(r)
