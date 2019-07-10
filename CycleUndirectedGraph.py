# Find a cycle in undirected graph using dfs
# O(V+E)

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

  def cycle(self):
    visited = set()
    # test all keys since this is not a search its a cycle test
    for key in self.root:
      if key not in visited:
        if self._cycle(visited, key, -1):
          print('cycle found with key: ', key)
        else:
          print('no cycle found with key:', key)

  def _cycle(self, visited, key, parent):

    visited.add(key)
    for neighbour in self.root[key].neighbours:
      print(key, neighbour)
      if neighbour not in visited:
        if self._cycle(visited, neighbour, key):
          return True
      elif parent != neighbour:
        return True
  
    return False


if __name__ == '__main__':
  a = graph()
  a.addnode(0,1)
  a.addnode(0,2)
  a.addnode(1,3)
  a.addnode(1,4)
  a.addnode(2,4)
  a.addnode(4,5)
  a.cycle()
  b = graph()
  b.addnode('a','b')
  b.addnode('a','c')
  b.addnode('b','d')
  b.addnode('b','e')
  b.cycle()



    




