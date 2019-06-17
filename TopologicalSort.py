# topological sort using Tarjans algorithm

class node:

  def __init__(self, key):
    self.key = key
    self.neighbours = {}
  
  def add(self, key, edge):
    self.neighbours[key] = edge
  
class dirgraph:

  def __init__(self):
    
    self.nodes = {}
  
  def add(self, key1, key2, edge=0):
    
    if key1 not in self.nodes:
      self.nodes[key1] = node(key1)
    if key2 not in self.nodes:
      self.nodes[key2] = node(key2)
    self.nodes[key1].add(key2, edge)

  def topologicalsort(self):
    
    print('beginning topological sort')

    visited = set()
    stack = []

    for key in self.nodes:
      if key not in visited:
        self._topologicalsort(key, visited, stack)
    
    print(stack)
  
  def _topologicalsort(self, key, visited, stack):

    visited.add(key)

    for neighbour in self.nodes[key].neighbours:
      if neighbour not in visited:
        self._topologicalsort(neighbour, visited, stack)

    stack.insert(0,key)
      
if __name__ == '__main__':
      a = dirgraph()
      a.add(5,2)
      a.add(4,0)
      a.add(5,0)
      a.add(4,1)
      a.add(2,3)
      a.add(3,1)
      a.topologicalsort()
