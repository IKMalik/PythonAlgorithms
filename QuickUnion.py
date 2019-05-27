class QuickUnion:

  vals = []
  size = []

  def __init__(self,n):

    self.vals = [i for i in range (0,n)]
    self.size = [1 for j in range (0,n)]

  def GetRoot(self, i):

    while (i != self.vals[i]):
      self.vals[i] = self.vals[self.vals[i]]
      i = self.vals[i]
    return i
  
  def Connected(self, i, j):

    return (self.GetRoot(i) == self.GetRoot(j))
  
  def Union(self, i, j):
    
    if (not self.Connected(i,j)):
      if (self.size[i] < self.size[j]):
        self.vals[self.GetRoot(i)] = self.vals[self.GetRoot(j)]
        self.size[j] += self.size[i]
      else:
        self.vals[self.GetRoot(j)] = self.vals[self.GetRoot(i)]
        self.size[i] += self.size[j]

if __name__ == "__main__":
  A = QuickUnion(6)
  A.GetRoot(2)
  A.Union(1,2)
  A.Union(3,4)
  A.Union(1,5)
  A.Union(1,3)
  print(A.vals)
  print(A.size)

