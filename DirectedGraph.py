
class vertex:

  def __init__(self, key):

    self.neighbours = {}
    self.key = key
  
  def add(self, key, edge):
    self.neighbours[key] = edge

class graph:

  def __init__(self):

    self.root = {}
    self.nbnodes = 0

  def addnode(self, key1, key2, edge=0):
    if key1 not in self.root:
      self.root[key1] = vertex(key1)
      self.nbnodes += 1
    if key2 not in self.root:
      self.root[key2] = vertex(key2)
      self.nbnodes += 1

    self.root[key1].add(key2, edge)
