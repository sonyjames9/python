"""
Hashtable functions

put(key,val)
get(key)
del
len()
in
"""


from tracemalloc import start
from turtle import position


class HashTable():

  def __init__(self, size) -> None:
    self.size = size
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def put(self, key, data):
    hash_value = self.hash_function(key, len(self.slots))

    if self.slots[hash_value] == None:
      self.slots[hash_value] = key
      self.data[hash_value] = data
    elif self.slots[hash_value] == key:
        self.data[hash_value] = data
    else:
      next_slot = self.rehash(hash_value, len(self.slots))
      while self.slots[next_slot] != None and self.slots[next_slot] != key:
        next_slot = self.rehash(next_slot, len(self.slots))
      if self.slots[next_slot] == None:
        self.slots[next_slot] = key
        self.data[next_slot] = data
      else:
        self.data[next_slot] = data

  def hash_function(self, key, size):
    return key % size

  def rehash(self, old_hash_value, size):
    return (old_hash_value+1) % size

  def get(self, key):
    start_slot = self.hash_function(key, len(self.slots))
    data = None
    stop = False
    found = False
    position = start_slot

    while self.slots[position] != None and not found and not stop:
      if self.slots[position] == key:
        found = True
        data = self.data[position]
      else:
        position = self.rehash(position, len(self.slots))
        if position == start_slot:
          stop = True

    return data

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, data):
    self.put(key, data)


hash_table = HashTable(5)
hash_table[1] = 'one'
hash_table[2] = 'two'
hash_table[3] = 'three'

print(hash_table[1])
print(hash_table[2])
