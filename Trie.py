# Prefix Tree / Trie code

class node:

  def __init__(self):

    self.children = {}
    self.isword = False
  
class trie:

  def __init__(self):

    self.root = None
  
  def insert(self, key):

    current = self.root
    for char in key:
      if char not in current.children:
        current.children[char] = node()
      current = current.children[char]
    current.isword = True
  
  def get(self, key):

    current = self.root
    for char in key:
      if char not in current.children:
        return False
      current = current.children[char]
    return current.isword 
  

