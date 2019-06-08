# 19/7/18 fixed ceil bug
# 19/7/18 added size method, which returns numbers nodes in a subtree (by default set to number nodes in tree) 
# 19/7/18 added rank function/ all keys < k 
# 20/7/18 added inorder traversal to view nodes
# 26/7/18 refactored naming conventions
# 26/7/18 fixed delete min rec bug
# 27/7/18 Added find min function and completed delete key function // hibbard deletion  
# need to keep in mind scope and return nature in recursive functions
# 27/7/18 Fixed insidious bug in find min // return bug 
# 30/5/19 Fixed major bug in insert 
# 6/6/19 Added put method as better alternative to insert
# 8/6/19 Overhauled many methods fixing many bugs 

#binary search tree


class Node():

  def __init__(self, key, value):

    self.key = key
    self.value = value
    self.count = 0
    self.left = None
    self.right = None

class BST():

  def __init__(self):

    self.root = None
  
  def get(self, key):

    if self.root is None:
      return None
    else:

      current = self.root
      while (current != None):

        if key == current.key:
          print('key found')
          return current.value
        elif key > current.key:
          current = current.right
        else:
          current = current.left
      
      return None

  def put(self, key, value):
    
    self.root = self._put(self.root, key, value)

  def _put(self, node, key, value):

    if node is None:
      node = Node (key, value)

    elif key == node.key:
      node.value = value

    elif key > node.key:
      node.right = self._put(node.right, key, value)

    else:
      node.left = self._put(node.left, key, value)
    
    node.count = 1 + self._size(node.left) + self._size(node.right)
    return node
  
  def size(self):

    if self.root is None:
      return None
    else:
      print ('size of root node is: ', self.root.count)
      return 
  
  def _size(self, node):

    if node is None:
      return 0
    else:
      return node.count

  def floor(self, key):

    resultnode = self._floor(self.root, key)
    if resultnode is None:
      return None
    else:
      print('floor key is: ', resultnode.key)
      return resultnode.key
  
  def _floor(self, node, key):

    if node is None:
      return None
    
    elif node.key == key:
      return node 
    
    elif node.key > key:
      return self._floor(node.left, key)
      
    else:
      altnode = self._floor(node.right, key)
      if altnode is None:
        return node
      else:
        return altnode
  
  def rank(self, key):

    size = self._rank(self.root, key)
    print('rank of key is: ', size )
  
  def _rank(self, node, key):

    if node is None:
      return 0
    elif node.key == key:
      return self._size(node.left)
    elif node.key > key:
      return self._rank(node.left, key)
    else: 
      return 1 + self._size(node.left) + self._rank(node.right, key)
  
  def delete(self, key):
    
    self.root = self._delete(self.root, key)

  def _delete(self, node, key):

    if node is None:
      return None
    elif key < node.key:
      node.left = self._delete(node.left, key)
    elif key > node.key:
      node.right = self._delete(node.right, key)
    # key found
    else:
      if node.left is None:
        return node.right
      if node.right is None:
        return node.left
      else:
        tempnode = node
        node = self.getchild(node.right)      
        node.left = tempnode.left
        node.right = self._delete(tempnode.right, node.key)
    return node
  
  def getchild(self, node):
    while node.left is not None:
      node = node.left
    return node
  

if __name__ == '__main__':
  a = BST()
  a.put(7,7)
  a.put(3,3)
  a.put(10,10)
  a.put(1,1)
  a.put(5,5)
  a.put(8,8)
  a.get(5)
  a.get(10)
  a.size()
  a.floor(6)
  a.floor(8)
  a.rank(7)
  a.rank(3)
  a.rank(1)
  a.delete(3)
  a.get(3)
  a.get(5)

            
