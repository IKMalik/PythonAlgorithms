
class node():

    def __init__(self):

        self.data = None
        self.nextnode = None

class linkedlist():

    def __init__(self):

        self.headnode = None

    def insert(self, data): 

        newnode = node()
        newnode.data = data
        if self.headnode is None:      
            self.headnode = newnode
        else:
            newnode.nextnode = self.headnode
            self.headnode = newnode            

    def size(self): 

        startnode = self.headnode
        count = 0
        while(startnode is not None):
            count += 1
            startnode = startnode.nextnode
        return count

    def search(self, data):

        isfound = False
        currentnode = self.headnode
        while(currentnode.data != data):
            if (currentnode.nextnode == None):
                return isfound
                break
            currentnode = currentnode.nextnode
        isfound = True
        return isfound

    def delete(self,data):

        currentnode = self.headnode
        previousnode = None
        founddata = False

        while (currentnode is not None and founddata is False):
             if (currentnode.data == data):
                 founddata = True
             else:
                 previousnode = currentnode
                 currentnode = currentnode.nextnode
        
        if currentnode is None:
            raise ValueError("Data does not exist")
        elif (previousnode is None):
            self.headnode = self.headnode.nextnode
        else:
            previousnode.nextnode = currentnode.nextnode

if __name__ == "__main__":

    a = linkedlist()
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.delete(7)
    a.size()



        

    


