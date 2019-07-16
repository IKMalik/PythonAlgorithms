# List graph used as dict is unordered data struc

class graph:

  def __init__(self):

    self.graph = []
    self.edges = []
    self.parents = {}
    self.size = {}

  def addnode(self, key1, key2, edge=0):

    if key1 not in self.graph:
      self.graph.append(key1)
    if key2 not in self.graph:
      self.graph.append(key2)

    self.edges.append([key1, key2, edge])
  
  def getparent(self, vertex):

    while self.parents[vertex] != -1:
      vertex = self.parents[vertex]
    
    return vertex

  def union(self, vertex, neighbour):

    x_par = self.getparent(vertex)
    y_par = self.getparent(neighbour)
    if self.size[x_par] <= self.size[y_par]:
      self.parents[x_par] = y_par
      self.size[y_par] += self.size[x_par]
    else:
      self.parents[y_par] = x_par
      self.size[x_par] += self.size[y_par]

  def kruskal(self):

    mst = []
    total = 0

    for key in self.graph:
      self.parents[key] = -1
      self.size[key] = 1
    
    self.edges.sort(key = lambda x:x[2])

    for edge in self.edges:
        vertex, neighbour, weight_edge = edge
        x_par = self.getparent(vertex)
        y_par = self.getparent(neighbour)
        if x_par != y_par:
          self.union(x_par, y_par)
          mst.append(edge)
          total += weight_edge
    
    print(mst)
    print('mst of weight:', total)

  
g = graph() 
g.addnode(0, 1, 10) 
g.addnode(0, 2, 6) 
g.addnode(0, 3, 5) 
g.addnode(1, 3, 15) 
g.addnode(2, 3, 4) 
g.kruskal()
    



    

