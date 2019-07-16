# check cycles in graph using union find

from collections import defaultdict
class graph:

  def __init__(self):

    self.graph = defaultdict(list)

  def addnode(self, key1, key2, edge=0):
    if key2 not in self.graph:
      self.graph[key2] = []

    self.graph[key1].append(key2)
  
  def findcycle(self):

    parents = {}
    for key in self.graph:
      parents[key] = -1
    
    for vertex in self.graph:
      for neighbour in self.graph[vertex]:
        x_par = self.getparent(vertex, parents)
        y_par = self.getparent(neighbour, parents)
        if x_par == y_par:
          return True
        self.union(x_par, y_par, parents)
  
  def getparent(self, vertex, parents):

    if parents[vertex] == -1:
      return vertex
    else:
      return self.getparent(parents[vertex], parents)
  
  def union(self, vertex, neighbour, parents):

    x_par = self.getparent(vertex, parents)
    y_par = self.getparent(neighbour, parents)
    parents[x_par] = y_par

g = graph() 
g.addnode(0, 1) 
g.addnode(1, 2) 
g.addnode(2, 3) 
  
if g.findcycle(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")
    
