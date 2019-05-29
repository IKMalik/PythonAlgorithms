
class Binaryheap():

    def __init__(self):

        self.heap = [0] # heap starts at 1st pos in array
        self.length = 0

    def addnode(self, data):

        self.heap.append(data)
        self.length += 1
        if self.length > 0:
            self.swimnode(self.length)
        print(self.heap)

    def deletemin(self):
        print('head node removed', self.heap[1])
        self.heap[1] = self.heap[self.length]
        self.length -= 1
        self.heap.pop()
        self.sinknode(1)
        print(self.heap)

    def swimnode(self, position):

        while position//2 > 0:

            if self.heap[position] < self.heap[position // 2]:

                self.heap[position], self.heap[position//2] = self.heap[position//2], self.heap[position]

            position //= 2
        
    def sinknode(self, position):
        
        while (position*2) < self.length:
            smallestchild = self.minchild(position)
            if self.heap[smallestchild] < self.heap[position]:
                self.heap[smallestchild], self.heap[position] = self.heap[position], self.heap[smallestchild]
            
            position *= 2
                    
    def minchild(self, position): 

        if (position*2)+1 > self.length:
            return position*2

        else:
            if self.heap[position*2] < self.heap[(position*2)+1]:
                return position*2
            else:
                return (position*2) + 1
            
        
if __name__ == '__main__':

    a = Binaryheap()
    a.addnode(3)
    a.addnode(6)
    a.addnode(9)
    a.addnode(1)
    a.addnode(11)
    a.addnode(23)
    a.addnode(7)
    a.deletemin()
    a.deletemin()
    a.addnode(1)
    
 
class BinaryHeap():

  def __init__(self):
    self.heap = [0]
    self.size = 0
  
  def insert(self, key):

    self.size += 1
    self.heap.append(key)
    print (self.heap)
    self.swim(self.size)
    print (self.heap)
  
  def swim(self, key):
    while (key > 1 and self.heap[key] > self.heap[key//2]):
      self.heap[key], self.heap[key//2] = self.heap[key//2], self.heap[key]
      key = key//2
  
  def delmin(self):
    key = self.heap[1]
    self.heap[1] = self.heap[self.size]
    self.heap[self.size] = None
    print(self.heap)
    self.skin(1)
    print(self.heap)
  
  def sink(self, key):
    while(self.heap[key] < self.heap[2*key])
    

        
