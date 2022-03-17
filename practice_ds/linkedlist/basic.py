from soupsieve import escape


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinedList:
    def __init__(self) -> None:
        self.head = None
        
    def insertNode(self,node):
        if self.head == None:
            self.head = node
        else:
            try:
                self.insertNodeAtEnd(node)
            except:
                self.head.next = node
        
    def insertNodeAtStart(self,node):
        if self.head == None:
            self.head.next = node
        else:
            node.next = self.head
            self.head = node
            
    def printData(self):
        nodevalue = self.head
        while nodevalue != None:
            print(nodevalue.data)
            nodevalue = nodevalue.next
    
    def insertNodeAtEnd(self,node):
        if self.head == None:
            self.head = node
        else:
            nodevalue = self.head
            while nodevalue != None:
                print(nodevalue.data)
                nodevalue = nodevalue.next
            nodevalue.next = node
        

if __name__ == '__main__':
    linkedlist = LinedList()
    linkedlist.insertNode(Node(1))
    linkedlist.printData()
    linkedlist.insertNode(Node(2))
    linkedlist.insertNode(Node(3))
    
    two = Node(2)
    three = Node(3)
    linkedlist.head.next = two
    two.next = three
    nodevalue = linkedlist.head
    while nodevalue != None:
        print(nodevalue.data)
        nodevalue = nodevalue.next
        
    # insert new node in start of the linkedlist
    newNode = Node(0)
    if linkedlist.head != None:
        newNode.next = linkedlist.head
        linkedlist.head = newNode
        
    # insert new node in end  of the linkedlist
    newNode = Node(5)
    if linkedlist.head != None:
        while nodevalue != None:
            nodevalue = nodevalue.next
        nodevalue.next = newNode
    