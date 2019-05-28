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
    
    self.headnode = None
  
  def push(self, data):

    anode = Node(data)
    if self.headnode is None:
      self.headnode = anode
    else:
      anode.nextnode = self.headnode.nextnode
      self.headnode = anode

  def pop(self):

    if self.headnode is None:
      return None
    else:
      data = self.headnode.data
      self.headnode = self.headnode.nextnode
      return data

class Queue:

  def __init__(self):
    
    self.headnode = None
  
  def enqueue(self, data):

    anode = Node(data)
    if self.headnode is None:
      self.headnode = anode
    else:
      nextn = self.headnode
      while (nextn.nextnode is not None):
        nextn = nextn.nextnode
      nextn.nextnode = anode 

  def dequeue(self):

    if self.headnode is None:
      return None
    else:
      data = self.headnode.data
      self.headnode = self.headnode.nextnode
      return data
      
