class Graph: 
   
    def __init__(self): 

        self.graph = {}

    def addEdge(self,u,v):
        if u not in self.graph:
          self.graph[u] = []
        if v not in self.graph:
          self.graph[v] = []
     
        self.graph[u].append(v) 
  
    def printscc(self):

      visited = set()
      stack = []

      for vertex in self.graph:
        if vertex not in visited:
          self._dfs(vertex, visited, stack)
      
      gr = self._invertgraph()

      visited.clear()

      print('finding scc \n')
      while stack:
          curr = stack.pop()
          if curr not in visited:
            gr._getscc(curr, visited)
            print("")
    
    def _dfs(self, vertex, visited, stack):

      visited.add(vertex)
      for neighbour in self.graph[vertex]:
        if neighbour not in visited:
          self._dfs(neighbour, visited, stack)
      stack.append(vertex)
    
    def _getscc(self, curr, visited):

      visited.add(curr)
      print(curr)
      for neighbour in self.graph[curr]:
        if neighbour not in visited:
          self._getscc(neighbour, visited)     

    def _invertgraph(self):
      
      gr = Graph()
      print(self.graph)
      for vertex in self.graph:
        for neighbour in self.graph[vertex]:
          gr.addEdge(neighbour, vertex)
      return gr



g = Graph() 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
g.printscc() 
