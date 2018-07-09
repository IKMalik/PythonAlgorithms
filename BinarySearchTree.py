#binary search tree


class node():

    def __init__(self, key, data):

        self.data = data
        self.key = key
        self.leftnode = None
        self.rightnode = None


class binarysearch():

    def __init__(self):

        self.size = 0
        self.rootnode = None

    def insertroot(self, key, data):

        if self.rootnode == None:
            self.rootnode = node(key, data)
        else:
            self.insertnode(self.rootnode, key, data)


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

    def searchkey(self, root, key):

        if root == None:
            return False
            
        else:
            if key == root.key:
                return True

            elif key < root.key:
                self.searchkey(root.leftnode, key)

            else:
                self.searchkey(root.rightnode, key)
                
    def floor(self, root, key): # largest value smaller than key

        if root.key == None:
            return None

        elif root.key == key:
            return key

        elif root.key > key:
            floor(root.lefttnode, key)

        else: # stop when find root that could be floor, now either rightsubtree or root is the floor.
            
            floorval = floor(root.rightnode, key)
            if floorval <= key:
                return floorval
            else:
                return root.key


    def ceil(self, root, key): # largest key <= key

        if root.key == None:
            return None

        elif root.key == key:
            return root

        elif root.key < key:
            return self.ceil(root.rightnode, key)

        else: # ceil is this node or in left subtreee
            
            ceilnode = self.ceil(root.leftnode, key)
            if ceilnode >= key:
                return ceilnode
            else:
                return root.key
            
