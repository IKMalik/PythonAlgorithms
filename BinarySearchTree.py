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
                
            
