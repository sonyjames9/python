import math


class BinaryTree():
  def __init__(self, val) -> None:
      self.val = val
      self.left_child = None
      self.right_child = None

  def insert_left(self, new_node):
    # Insert left
    # When there is no left child, we are adding node to the tree
    if self.left_child == None:
      self.left_child = BinaryTree(new_node)
    # If there is existing left node, then to add another left node
    # we push the existing child one level in the tree
    else:
      left_node = BinaryTree(new_node)
      left_node.left_child = self.left_child
      self.left_child = left_node

  def insert_right(self, new_node):
    if self.right_child == None:
      self.right_child = BinaryTree(new_node)
    else:
      right_node = BinaryTree(new_node)
      right_node.right_child = self.right_child
      self.right_child = right_node

  def get_right_child(self):
    return self.right_child

  def get_left_child(self):
    return self.left_child

  def set_root_val(self, obj):
    self.val = obj

  def get_root_val(self):
    return self.val

  # Check if the BST is valid
  def is_valid_bst(self, root):
    return self.is_valid(root, -math.inf, math.inf)

  def is_valid(self, root, min_val, max_val):
    if root is None:
      return True
    else:
      return (root.val > min_val and root.val < max_val and self.is_valid(root.left_child, min_val, root.val) and self.is_valid(root.right_child, root.val, max_val))


r = BinaryTree('a')
print(r.get_root_val())
r.get_root_val()

r.insert_left('b')
r.get_left_child().get_root_val()
