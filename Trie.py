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


## Itterating a full trie example

class Node:
    
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.fullword = None

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        # add all to trie O(chars)
        # run through trie to get smallest word O(chars)
        
        trie = Node()
        
        for word in words:
            
            cur = trie
            
            for char in word:
                
                if char not in cur.children:
                    cur.children[char] = Node()
                cur = cur.children[char]
            cur.isWord = True
            cur.fullword = word 
        
        res = ["", -1]
        
        self.itterTrie(trie, res)
        
        return res[0]
        
        
    def itterTrie(self, trie, res):
        
        for child in trie.children:
            
            cur = trie.children[child]
            
            if cur.isWord:
                curLen = len(cur.fullword)
                
                if curLen == res[1]:
                    res[0] = min(res[0], cur.fullword)
                elif curLen > res[1]:
                    res[0] = cur.fullword
                    res[1] = curLen
                
                self.itterTrie(cur, res)
