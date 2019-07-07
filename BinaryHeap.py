# max binary heap
# 0th pos not used

class BinaryHeap():

  def __init__(self):
    self.heap = [0]
    self.size = 0
  
  def insert(self, key):

    self.size += 1
    self.heap.append(key)
    self.swim(self.size)
  
  def swim(self, key):
    while (key > 1 and self.heap[key] > self.heap[key//2]):
      self.heap[key], self.heap[key//2] = self.heap[key//2], self.heap[key]
      key = key//2
  
  def delmax(self):
    self.heap.pop()
    self.heap[1] = self.heap[self.size]
    self.size -= 1
    self.sink(1)
  
  def sink(self, key):
    while(2*key <= self.size):
      bigchild = self.largest(key)
      if self.heap[key] < self.heap[bigchild]:
        self.heap[key], self.heap[bigchild] = self.heap[bigchild], self.heap[key]
      key = bigchild
  
  def largest(self, key):
    if (2*key)+1 > self.size:
      return 2*key
    if self.heap[2*key] > self.heap[(2*key)+1]:
      return 2*key
    else:
      return (2*key) + 1
