class QueueImpl():
  """
  First in First out principle

  Stack Implementations ---

  is_empty
  enqueue
  dequeue
  """

  def __init__(self) -> None:
    self.items = []

  def is_empty(self):
    return self.items == []

  def enqueue_item(self, item):
    self.items.append(item)

  def deqeueue_item(self):
    return self.items.pop()

  def size(self):
    return len(self.items)


queue_obj = QueueImpl()
print("Queue length : {}".format(queue_obj.size()))
print("Queue isEmpty : {}".format(queue_obj.is_empty()))
queue_obj.enqueue_item('a')
queue_obj.enqueue_item('b')
queue_obj.enqueue_item('c')
print("Queue length : {}".format(queue_obj.size()))
queue_obj.deqeueue_item()
print("Queue length : {}".format(queue_obj.size()))
