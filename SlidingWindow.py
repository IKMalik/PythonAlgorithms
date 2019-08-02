

def sliding(word, chars):

  left = right = 0
  visited = {}
  bestscore = float('inf')
  setchars_met = 0
  
  while right < len(word) or setchars_met == len(chars) :
    
    if setchars_met != len(chars):
      curr_right = word[right]
      if curr_right in chars:
        visited.setdefault(curr_right, 0)
        visited[curr_right] += 1
        if visited[curr_right] == 1:
          setchars_met += 1
      right += 1

    else:
      curr_left = word[left]
      if curr_left in chars:
        visited[curr_left] -= 1
        if visited[curr_left] == 0:
          setchars_met -= 1
      left += 1
    
      bestscore = min(bestscore, right - left + 1)
      print(bestscore, right, left)
  print (bestscore)


s = 'abczdacb'
sets = ('a', 'b', 'c', 'd')
sliding(s,sets )
