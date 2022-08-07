class BinaryHeap:
  def __init__(self) -> None:
    self.heap_lists = [0]
    self.current_size = [0]

  def perc_up(self, i):
    while i // 2 > 0:
      if self.heap_lists[i] < self.heap_lists[i // 2]:
        tmp = self.heap_lists[i // 2]
        self.heap_lists[i // 2] = self.heap_lists[i]
        self.heap_lists[i] = tmp

      i = i // 2

  def insert(self, k):
    self.heap_lists.append(k)
    self.current_size = self.current_size + 1
    self.perc_up(self.current_size)

  def perc_down(self, i):
    while (i*2) <= self.current_size:
      mc = self.min_child(i)
      if self.heap_lists[i] > self.heap_lists[mc]:
        tmp = self.heap_lists[i]
        self.heap_lists[i] = self.heap_lists[mc]
        self.heap_lists[mc] = tmp
      i = mc

  def min_child(self, i):
    if (i * 2 + 1) > self.current_size:
      return (i * 2)
    else:
      if self.heap_lists[i*2] < self.heap_lists[i*2+1]:
        return (i*2)
      else:
        return (i*2+1)

  def del_min(self):
    ret_val = self.heap_lists[1]
    self.heap_lists[1] = self.heap_lists[self.current_size]
    self.current_size = self.current_size - 1
    self.heap_lists.pop()
    self.perc_down(1)
    return ret_val

  def build_heap(self, alist):
    i = len(alist) // 2
    self.current_size = len(alist)
    self.heap_lists = [0] + alist[:]
    while(i > 0):
      self.perc_down(i)
      i -= 1
