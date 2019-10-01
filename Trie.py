# Prefix Tree / Trie code

class TrieNode:

  def __init__(self):

    self.children = {}
    self.isWord = False

class Trie:

  def __init__(self):

    self.root = TrieNode()
  
  def add(self, word):

    curr = self.root 
    for char in word:
      if char not in curr.children:
        curr.children[char] = TrieNode()
      curr = curr.children[char]
    curr.isWord = True

  def get(self, word):

    curr = self.root
    for char in word:
      if char not in curr.children:
        return False
      curr = curr.children[char]
    print(curr.isWord)
    return curr.isWord

trie = Trie()
trie.add('bob')
trie.add('bed')
trie.get('bob')
trie.get('bed')
trie.get('be')
