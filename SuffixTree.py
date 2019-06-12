#simple suffix tree

class node:

  def __init__(self, key):

    self.children = {}
    self.isword = False
  
class SuffixTree:

  def __init__(self):

    self.root = node()
  
  def insert(self, word):

    current = self.root
    for char in word:
      if char not in current.children:
        current = node(char):
      current = current.children[char]
    current.isword = True
  
