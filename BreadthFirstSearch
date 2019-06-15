#BFS WITH ADJACENCY LIST
#TEST CASES WITH STRINGS AND INTS PROVIDED

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

  def bfs(self, key):
    
    queue = []
    visited = set()
    queue.append(key)
    visited.add(key)

    while queue: # while elements in queue
      nodekey = queue.pop(0)
      print('current key: ', nodekey)

      for neighbour in self.root[nodekey].neighbours:
        if neighbour not in visited:
          queue.append(neighbour)
          visited.add(neighbour)

if __name__ == '__main__':
  a = graph()
  a.addnode(0,1)
  a.addnode(0,2)
  a.addnode(1,3)
  a.addnode(1,4)
  a.addnode(2,4)
  a.addnode(4,5)
  a.bfs(0)
  b = graph()
  b.addnode('a','b')
  b.addnode('a','c')
  b.addnode('b','d')
  b.addnode('b','e')
  b.bfs('a')
