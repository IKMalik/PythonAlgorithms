EDIT: MORE FUNTIONAL CODE
  
def lcs(word1, word2):

  x = len(word1)
  y = len(word2)
  return _lcs(word1, word2, x, y)

def _lcs(word1, word2, x, y):

  # create matrix 

  matrix = [[-1]*(x) for val in range (0,y)]

  for i in range(0, x):
    for j in range(0, y):
      
      if word1[i] == word2[j]:
        matrix[i][j] = 1 + max(getmax(i-1, j, matrix), getmax(i, j-1, matrix))
      else: 
        matrix[i][j] = max(getmax(i-1, j, matrix), getmax(i, j-1, matrix))

  return matrix[x-1][y-1]

def getmax(a, b, matrix):

  if a < 0 or b < 0 :
    return 0
  else:
    return matrix[a][b]

b = 'aword'
a = 'wsrod'
print(lcs(a,b))

  
  
  
  
  
def lcs(word1, word2):

  x = len(word1)
  y = len(word2)
  return _lcs(word1, word2, x, y)

def _lcs(word1, word2, x, y):

  # create matrix 

  matrix = [[-1]*(x) for val in range (0,y)]

  for i in range(0, x):
    for j in range(0, y):
      
      if word1[i] == word2[j]:
        val1 = 0
        val2 = 0
        if i-1 >= 0:
          val1 = matrix[i-1][j]
        if j-1 >= 0:
          val2 = matrix[i][j-1]
        matrix[i][j] = 1 + max(val1,val2)

      else:
        val1 = 0
        val2 = 0
        if i-1 >= 0:
          val1 = matrix[i-1][j]
        if j-1 >= 0:
          val2 = matrix[i][j-1]
        matrix[i][j] = max(val1,val2)
  
  print(matrix)
  return matrix[x-1][y-1]

b = 'aword'
a = 'wsrod'
print(lcs(a,b))
