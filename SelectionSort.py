# class based

class SelectionSort():
    
    listints = []
    
    def SelectionSort(self, x):
        self.listints = x
        end = len(self.listints)

        for inta in range (0,end):
            minv = inta   
            for intb in range (inta+1,end):
                if self.listints[intb] < self.listints[minv]:
                    minv = intb
            self.swap(inta, minv)

        print (str(self.listints))

    def swap(self, oldmin, newmin):
        temphold =  self.listints[oldmin]
        self.listints[oldmin]  =  self.listints[newmin]
        self.listints[newmin] = temphold

    
if __name__=="__main__":
    A = SelectionSort()
    A.SelectionSort([21,3,7,12,19,4,3,5])


# code based

def SelectionSort(x):
        listints = x
        end = len(listints)

        for inta in range (0,end):
            minv = inta   
            for intb in range (inta+1,end):
                if listints[intb] < listints[minv]:
                    minv = intb
            temphold =  listints[inta]
            listints[inta]  =  listints[minv]
            listints[minv] = temphold
        print (str(listints))


SelectionSort([21,3,7,12,19,4,3,5])

