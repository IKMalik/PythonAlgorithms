EDIT: fixed bug counting repeated letters, e.g abb and abc would give 3 instead of 2
  
def lcs(word1, word2):

  x = len(word1)
  y = len(word2)
  return _lcs(word1, word2, x, y)

def _lcs(word1, word2, x, y):

  matrix = [ [None] * (x) for _ in range (y) ]

  for i in range(y):
    for j in range(x):
      
      if word1[j] == word2[i]:
        matrix[i][j] = 1
        if i > 0 and j > 0:
          matrix[i][j] += matrix[i-1][j-1]

      else:
        val1 = matrix[i-1][j] if i > 0 else 0
        val2 = matrix[i][j-1] if j > 0 else 0
        matrix[i][j] = max(val1,val2)
  
  return matrix[-1][-1]

a = 'ABC'
b = 'ABCD'
print(lcs(a,b))
