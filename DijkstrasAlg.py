O((V+E)logV) Implementation 

import heapq

def dijkstra(graph, start):

  distances = {vertex:float('inf') for vertex in graph}
  pq = []
  pq = [[0, start]]

  while pq:

    currdist, currvert = heapq.heappop(pq)

    if currdist > distances[currvert]:
      continue

    for neighbour, distance_neigh in graph[currvert].items():
      dist = currdist + distance_neigh

      if dist < distances[neighbour]:
        distances[neighbour] = dist
        heapq.heappush(pq, [dist, neighbour])

  print(distances)
  return distances 



if __name__ == '__main__':

  example_graph = {
      'U': {'V': 2, 'W': 5, 'X': 1},
      'V': {'U': 2, 'X': 2, 'W': 3},
      'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
      'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
      'Y': {'X': 1, 'W': 1, 'Z': 1},
      'Z': {'W': 5, 'Y': 1},
  }
  dijkstra(example_graph, 'X')
