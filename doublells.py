class Node:
    def __init__(self, data=None, next=None, prev =None):
        self.data =data
        self.next = next
        self.prev = prev

class lls:
    def __init__(self):
        self.head = None

    
    def print(self):
        if self.head is None:
            print("lls[] is empty")
        
        node = self.head
        itrstr = ""
        while node is not None:
            itrstr += node.data + "<--->"
            node.next
     
    def Addleft(self,data):
        if self.head is None:
            self.head= Node(self.data, next= None, prev=None)
            return

        itr = self.head

        while itr:
            itr = itr.next
            
        itr.next= Node(self.data, next=None, prev=self.head)



if __name__ == "__main__":
    circularlls = lls()

    circularlls.Addleft("root")