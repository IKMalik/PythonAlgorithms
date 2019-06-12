class node:

  def __init__(self, key):

    self.key = key
    self.neighbours = {}
  
  def addedge(self, key, edge):

    self.neighbours[key] = edge

  
class adjlist:

  def __init__(self):

    self.nodes = {}
    self.nbnodes 0
  
  def addnode(self, key):

    if key not in self.nodes:
      self.nodes[key] = node()
    self.nbnodes += 1
  
  def addedge(self, key1, key2, edge):

    if key1 not in self.nodes:
      self.addnode(key1)
    elif key2 not in self.nodes:
      self.addnode(key2)
    else:
      self.nodes[key1].addedge(key2, edge)
      self.nodes[key2].addedge(key1, edge)
    
