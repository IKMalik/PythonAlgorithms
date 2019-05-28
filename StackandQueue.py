#array implementation of stack and queue 

class Stack():

    def __init__(self):
        self.array_vals = []

    def push(self, value):
        self.array_vals.append(value)

    def pop(self):
        self.array_vals.pop()


class Queue():

    def __init__(self):
        self.list_vals = []

    def enqueue(self, value):
        self.list_vals.append(value)

    def dequeue(self):
        self.list_vals.pop(0)
        print(str(self.list_vals))
        
# Linked List implementation stack and queue 

class Node:

  def __init__(self, data):

    self.data = data
    self.nextnode = None

class Stack:

  def __init__(self):
    
    self.size = 0
    self.headnode = None
  
  def push(self, data):

    anode = Node(data)
    if self.headnode is None:
      self.headnode = anode
    else:
      anode.nextnode = self.headnode.nextnode
      self.headnode = anode
    self.size += 1

  def pop(self):

    if self.headnode is None:
      return None
    else:
      data = self.headnode.data
      self.headnode = self.headnode.nextnode
      self.size -= 1
      return data
  
  def size(self):

    return self.size
