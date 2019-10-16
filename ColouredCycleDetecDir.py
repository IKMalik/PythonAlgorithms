    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if prerequisites is None:
            return True
        
        graph = {}
        
        for key in range(numCourses):
            graph[key] = []
        
        for pre in prerequisites:
            
            start, end = pre
            graph[start].append(end)
        
        # white = unvisited = 0
        colours = [0 for _ in range(numCourses)]
        
        for course in range(numCourses):
            if colours[course] == 0:
                if self.isCyclic(course, graph, colours) == True: # if cycle is found
                    return False
        return True
        
    def isCyclic(self, course, graph, colours):
        
        # grey = visiting = 1
        colours[course] = 1
        
        for neighbour in graph[course]:
            
            # Cycle found 
            if colours[neighbour] == 1:
                return True
            
            if colours[neighbour] == 0 and self.isCyclic(neighbour, graph, colours) == True:
                return True
        
        # black = visited = -1
        colours[course] = -1
        return False
      
