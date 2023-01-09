class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next= next

class linkedlist:
    def __init__(self):
        self.head = None

    def add_left(self, new):
        new_node =Node(new,self.head)
        self.head = new_node
    

    
    def print(self):
        if self.head is None:
            print("linkedlist[]")
            return 
        
        
        itr = self.head
        itrStr = ""

        while itr:
            
            itrStr += str(itr.data) + "-->"
            itr = itr.next      
        print(itrStr) 

    def Add(self,data):
        if self.head is None:
          self.head = Node(data,next=None)
          return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self,values):
        if self.head is None:
            for value in values:
                self.Add(value)
        else:
            for value in values:
                self.Add(value)

    def insert_at_middle(self, values, value):
        itr = self.head
        count = 0
        while itr.next:
            count += 1
            if value == itr.data:
                print(f"The value is found at index {count} and the value is {itr.data}")
            itr = itr.next
    
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next  
        return count
    
    def remove_at(self, index):
        if index < 0 or  index>= self.get_length():
            print("The index is out of bound")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1 :
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def remove_by_value(self,data):
        itr = self.head
        count = 0

        if itr == data:
            itr == itr.next

        while itr:

            

            itr = itr.next
            count +=1
            
            
            

        



if __name__ == "__main__":
    link = linkedlist()
    link.insert_values(["tomatoes","mangoes"])
    link.Add(4)
    link.print()
    link.remove_at(1)
    link.print()

    print(link.get_length())
    