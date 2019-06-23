EDIT: fixed bug counting repeated letters, e.g abb and abc would give 3 instead of 2
  
def lcs(word1, word2):

  x = len(word1)
  y = len(word2)
  return _lcs(word1, word2, x, y)

def _lcs(word1, word2, x, y):

  # create matrix 

  matrix = [[-1]*(x) for val in range (0,y)]

  for i in range(0, y):
    for j in range(0, x):
      
      if word1[j] == word2[i]:
        if i-1 < 0 or j-1 < 0:
          matrix[i][j] = 1 
        else:
          matrix[i][j] = 1 + matrix[i-1][j-1]

      else:
        val1 = 0
        val2 = 0
        if i-1 >= 0:
          val1 = matrix[i-1][j]
        if j-1 >= 0:
          val2 = matrix[i][j-1]
        matrix[i][j] = max(val1,val2)
  
  return matrix[y-1][x-1]

a = 'ABC'
b = 'ABCD'
print(lcs(a,b))
