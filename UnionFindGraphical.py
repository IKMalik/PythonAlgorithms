# check cycles in graph using union find
# weighted tree balancing added
# path compress added


from collections import defaultdict
class graph:

  def __init__(self):

    self.graph = defaultdict(list)
    self.parents = {}
    self.size = {}

  def addnode(self, key1, key2, edge=0):
    if key2 not in self.graph:
      self.graph[key2] = []

    self.graph[key1].append(key2)
  
  def findcycle(self):


    for key in self.graph:
      self.parents[key] = -1
      self.size[key] = 1

    
    for vertex in self.graph:
      for neighbour in self.graph[vertex]:
        x_par = self.getparent(vertex)
        y_par = self.getparent(neighbour)
        if x_par == y_par:
          return True
        self.union(x_par, y_par)
  
  
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

g = graph() 
g.addnode(0, 1)  
g.addnode(2, 3) 
g.addnode(4,2)
g.addnode(4,1)
  
if g.findcycle(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")
    



    

