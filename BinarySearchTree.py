# 19/7/18 fixed ceil bug
# 19/7/18 added size method, which returns numbers nodes in a subtree (by default set to number nodes in tree) 
# 19/7/18 added rank function/ all keys < k 
# 20/7/18 added inorder traversal to view nodes
# 26/7/18 refactored naming conventions
# 26/7/18 fixed delete min rec bug

#binary search tree


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

    def insert(self, key, data):

        if self.rootnode is None:
            self.rootnode = anode(key, data)
        else:
            self.insertnode(self.rootnode, key, data)

    def getroot(self):

        return self.rootnode

    def insertnode(self, node, key, data):

            if node.key == key:
                node.data = data
                
            elif key < node.key:
                if node.leftnode is None:                    
                    node.leftnode = anode(key, data)
                else:
                    self.insertnode(node.leftnode, key, data)
            else:
                if node.rightnode is None:
                    node.rightnode = anode(key, data)
                else:
                    self.insertnode(node.rightnode, key, data)

            node.count = 1 + self.sizenode(node.leftnode) + self.sizenode(node.rightnode)

    def getsize(self):
        print (self.rootnode.count)

    def sizenode(self, node):

        if node is None:
            return 0
        else:
            return node.count

    def searchkey(self, key):

        if self.rootnode is None:
            return False
        else:
            found = self.searchnode(self.rootnode, key)
            if found:
                return True
            else:
                return False

    def searchnode(self, node, key):
        
        if node is None:
            return False
            
        else:
            if key == node.key:
                return True

            elif key < node.key:
                self.searchnode(node.leftnode, key)

            else:
                self.searchnode(node.rightnode, key)
        
                
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

    def ranknode(self, node, key): # number keys < key 

        if node is None:
            return 0
        
        else:
            
            if node.key == key:
                return self.sizenode(node.leftnode)

            elif root.key > key:
                return self.ranknode(node.leftnode, key) 
                
            else:
                return 1 + self.sizenode(node.leftnode) + self.ranknode(node.rightnode, key)
                
    def getrank(self, key):

        if self.rootnode is None:
            return 0
        else:
            print( self.ranknode(self.rootnode, key))

    def getnodes(self):
        
        if self.rootnode is None:
            print("No nodes exist")
        else:
            print("getting nodes")
            self.inorder(self.rootnode)


    def inorder(self, node):

        if node is not None:

            self.inorder(node.leftnode)
            print(node.key)
            self.inorder(node.rightnode)

    def deletemin(self):

        if self.rootnode is None:
            print("No nodes exist")
        else:
            self.rootnode = self.deleteminnode(self.rootnode)

    def deleteminnode(self, node):

        if node.leftnode is not None:
            node.leftnode = self.deleteminnode(node.leftnode)
            return node
        else:
            return node.rightnode
        

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
            
