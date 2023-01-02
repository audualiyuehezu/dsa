class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
    
    def leftAdd(self, new):
         node = Node(new,self.head)
         self.head = node
    
    def print(self):
        if self.head is None:
            print("linkedlist[]")
            return

        itr = self.head
        itrStr = " "
        

        while itr:
            itrStr += itr.data + " --> "
            itr = itr.next

        print(itrStr)

if __name__ == "__main__":
    link = linkedlist()

    link.leftAdd("c++")
    link.leftAdd("frosh")


    link.print()

