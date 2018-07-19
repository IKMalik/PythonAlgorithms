#binary search tree


class node():

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
            self.rootnode = node(key, data)
        else:
            self.insertnode(self.rootnode, key, data)

    def getroot(self):

        return self.rootnode

    def insertnode(self, root, key, data):

            if root.key == key:
                root.data = data
                
            elif key < root.key:
                if root.leftnode is None:                    
                    root.leftnode = node(key, data)
                else:
                    self.insertnode(root.leftnode, key, data)
            else:
                if root.rightnode is None:
                    root.rightnode = node(key, data)
                else:
                    self.insertnode(root.rightnode, key, data)

            root.count = 1 + self.sizenode(root.leftnode) + self.sizenode(root.rightnode)

    def getsize(self):
        print (self.rootnode.count)

    def sizenode(self, root):

        if root is None:
            return 0
        else:
            return root.count

    def searchkey(self, key):

        if self.rootnode is None:
            return False
        else:
            found = self.searchnode(self.rootnode, key)
            if found:
                return True
            else:
                return False

    def searchnode(self, root, key):
        
        if root is None:
            return False
            
        else:
            if key == root.key:
                return True

            elif key < root.key:
                self.searchnode(root.leftnode, key)

            else:
                self.searchnode(root.rightnode, key)
        
                
    def floor(self, root, key): 

        if root is None:
            return None

        elif root.key == key:
            return key

        elif root.key > key:
            return self.floor(root.leftnode, key)

        else:
            floorkey = self.floor(root.rightnode, key)
            if (floorkey is None) or (floorkey > key):
                return root.key 
            else:
                return floorkey

    def ceil(self, root, key): 

        if root == None:
            return None

        elif root.key == key:
            return key

        elif root.key < key:
            return self.ceil(root.rightnode, key)

        else:             
            ceilkey = self.ceil(root.leftnode, key)
            if (ceilkey is None) or (ceilkey < key):
                return root.key
            else:
                return ceilkey
            
