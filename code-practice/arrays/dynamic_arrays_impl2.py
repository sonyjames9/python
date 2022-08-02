from hashlib import new


class DynamicArray():
  def __init__(self) -> None:
    # actual number of elements in dynamic array
    self.size = 0
    # maximum capacity of the dynamic array
    self.capacity = 1
    self.array = self._create_array(self.capacity)

  def __len__(self):
    '''
    len(array): returns the length of the array
    '''
    return self.size

  def __getitem__(self, index):
    '''
    array[index]: returns the element at given index
    '''
    if not 0 < index < self.size:
      return IndexError('Given index : {0} is larger than array size {1}'.format(index, self.size))

    return self.array[index]

  def _create_array(self, length):
    '''
    create the array with given size
    '''
    return [None] * length

  def _resize(self, new_capacity):
    '''
    resize the array to the new capacity
    '''
    new_array = self._create_array(new_capacity)

    # reassign the elements in the old array into the new array
    for i in range(self.size):
      new_array[i] = self.array[i]

    self.array = new_array
    self.capacity = new_capacity

  def append(self, element):
    if self.size == self.capacity:
      self._resize(2 * self.capacity)

    self.array[self.size] = element
    self.size += 1

  def pop(self):
    element = None
    if self.size > 0:
      element = self.array[self.size - 1]
      self.array[self.size - 1] = None
      self.size -= 1

      if self.size <= self.capacity // 4:
        self._resize(self.capacity // 2)
    return element


da = DynamicArray()
da.append('a')
da.append('2')
da.append('r')
print(len(da))
