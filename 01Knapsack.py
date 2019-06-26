def knapsack(weights, values, maximum_weight):

  matrix = [ [0] * (1+maximum_weight) for _ in range( len(weights) ) ]

  for weight in range(len(weights)):

    for total in range(maximum_weight+1):

      # weight is possible inclusion
      if weights[weight] <= total:

        if weight > 0:
          matrix[weight][total] = max(values[weight] + matrix[weight-1][total-weights[weight]], matrix[weight-1][total])

        else:
          matrix[weight][total] = values[weight]

      # weight excluded 
      else:
          if weight > 0:
            matrix[weight][total] = matrix[weight-1][total]


  print(matrix)
  return matrix[-1][-1]


val = [1, 4, 5 ,7] 
wt = [1, 3, 4, 5] 
W = 7

print(knapsack(wt, val, W))
