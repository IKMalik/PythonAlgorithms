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

#binary search tree


class anode():

    def __init__(self, key, data):

        self.data = data
        self.key = key
        self.leftnode = None
        self.rightnode = None
        self.count = 1


class binarysearch():

    def __init__(self):

        self.size = 0
        self.rootnode = None

    def getroot(self):

        return self.rootnode

    def getsize(self):
        print (self.rootnode.count)

    def insert(self, key, data):

        if self.rootnode is None:
            self.rootnode = anode(key, data)
        else:
            self.rootnode = self._insert(self.rootnode, key, data)

    def _insert(self, node, key, data):

            if node.key == key:
                node.data = data
                
            elif key < node.key:
                if node.leftnode is None:                    
                    node.leftnode = anode(key, data)
                else:
                    self._insert(node.leftnode, key, data)
            else:
                if node.rightnode is None:
                    node.rightnode = anode(key, data)
                else:
                    self._insert(node.rightnode, key, data)

            node.count = 1 + self.sizenode(node.leftnode) + self.sizenode(node.rightnode)
            return node

    def sizenode(self, node):

        if node is None:
            return 0
        else:
            return node.count

    def searchkey(self, key):

        if self.rootnode is None:
            return False
        else:
            found = self._searchkey(self.rootnode, key)
            if found:
                return True
            else:
                return False

    def _searchkey(self, node, key):
        
        if node is None:
            return False
            
        else:
            if key == node.key:
                return True

            elif key < node.key:
                self._searchkey(node.leftnode, key)

            else:
                self._searchkey(node.rightnode, key)
        
                
    def floor(self, node, key): 

        if node is None:
            return None

        elif node.key == key:
            return key

        elif node.key > key:
            return self.floor(node.leftnode, key)

        else:
            floorkey = self.floor(node.rightnode, key)
            if (floorkey is None) or (floorkey > key):
                return node.key 
            else:
                return floorkey

    def ceil(self, node, key): 

        if node == None:
            return None

        elif node.key == key:
            return key

        elif node.key < key:
            return self.ceil(node.rightnode, key)

        else:             
            ceilkey = self.ceil(node.leftnode, key)
            if (ceilkey is None) or (ceilkey < key):
                return node.key
            else:
                return ceilkey
            
    def getrank(self, key): # number keys < key 

        if self.rootnode is None:
            return 0
        
        else:
            print( self._getrank(self.rootnode, key))

    def _getrank(self, node, key): 

        if node is None:
            return 0
        
        else:
            
            if node.key == key:
                return self.sizenode(node.leftnode)

            elif node.key > key:
                return self._getrank(node.leftnode, key) 
                
            else:
                return 1 + self.sizenode(node.leftnode) + self._getrank(node.rightnode, key)
            

    def getnodes(self):
        
        if self.rootnode is None:
            print("No nodes exist")
            
        else:
            print("getting nodes")
            self._getnodes(self.rootnode)


    def _getnodes(self, node):

        if node is not None:

            self._getnodes(node.leftnode)
            print(node.key)
            self._getnodes(node.rightnode)

    def findmin(self):

        if self.rootnode is not None:
            print( self._findmin(self.rootnode).key)

    def _findmin(self, node):

        if node.leftnode is None:
            return node
        else:
            return self._findmin(node.leftnode)

    def deletemin(self):

        if self.rootnode is None:
            print("No nodes exist")
            
        else:
            self.rootnode = self._deletemin(self.rootnode)

    def _deletemin(self, node):

        if node.leftnode is not None:
            node.leftnode = self._deletemin(node.leftnode)
            node.count = 1 + self.sizenode(node.leftnode) + self.sizenode(node.rightnode)
            return node
        
        else:
            return node.rightnode

    def deletekey(self, key):

        if self.rootnode is not None:
            self.rootnode = self._deletekey(self.rootnode, key)

    def _deletekey(self, node, key):


        if key > node.key:
            node.rightnode = self._deletekey(node.rightnode, key)
            
        elif key < node.key:
            node.leftnode = self._deletekey(node.leftnode, key)
            
        else:

            if node.leftnode == None:
                node = node.rightnode

            elif node.rightnode == None:
                node = node.leftnode

            else:
                tempnode = node
                node = self._findmin(node.rightnode)
                node.rightnode = self._deletemin(tempnode.rightnode)
                node.leftnode = tempnode.leftnode
                node.count = 1 + self.sizenode(node.leftnode) + self.sizenode(node.rightnode)
                
        return node

'''
if __name__ == '__main__':

    a = binarysearch()
    a.insert(7,7)
    a.insert(1,1)
    a.insert(0.5, 0.5)
    a.insert(0.25,0.25)
    a.insert(0.1, 0.1)
    a.insert(8,8)
    a.insert(3,3)
    a.insert(9,9)
    a.insert(2,2)
    a.insert(4,4)
    a.insert(3.5, 3.5)
    a.insert(5,5)
    a.insert(11,11)
    a.insert(10,10)
    a.deletekey(3)
    a.getnodes()
            

        
'''

if __name__ == '__main__':

    a = binarysearch()
    a.insert(7,7)
    a.insert(1,1)
    a.insert(0.5, 0.5)
    a.insert(8,8)
    a.insert(3,3)
    a.insert(9,9)
    a.insert(2,2)
    a.insert(4,4)
    a.insert(11,11)
    a.insert(10,10)
    a.searchkey(7)
    root = a.getroot()
    ceil = a.ceil(root, 10)
    print(ceil)
    floor = a.floor(root, 10)
    print(floor)
    a.getsize()
    a.getrank(8)
    a.getnodes()
    a.deletemin()
    a.getnodes()
            
