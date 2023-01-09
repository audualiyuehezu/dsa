"""
I want to create a custom linkedlist 
1. i want to create a node class
2. i want to create a linkedlist class
3. i want to write operations on it 
"""

class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
    def Add(self,value):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

link = linkedlist()


link.Add("c")
link.Add("value")
link.show()