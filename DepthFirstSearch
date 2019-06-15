#dfs WITH ADJACENCY LIST

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
    self.root[key2].add(key1, edge)

  def dfs(self, key):

    visited = set()
    self._dfs(key, visited)
  
  def _dfs(self, key, visited):

    visited.add(key)
    print(key)
    
    for neighbour in self.root[key].neighbours:
      if neighbour not in visited:
        self._dfs(neighbour, visited)


if __name__ == '__main__':
  a = graph()
  a.addnode(0,1)
  a.addnode(0,2)
  a.addnode(1,3)
  a.addnode(1,4)
  a.addnode(2,4)
  a.addnode(4,5)
  a.dfs(0)
  b = graph()
  b.addnode('a','b')
  b.addnode('a','c')
  b.addnode('b','d')
  b.addnode('b','e')
  b.dfs('a')



    




