


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
class LinedList:
    def __init__(self) -> None:
        self.head = None
        
        
linkedlist = LinedList()
linkedlist.head = Node(1)
linkedlist.head.next = Node(2)
linkedlist.head.next.next = Node(10)

linkedlist1 = LinedList()
linkedlist1.head = Node(2)
linkedlist1.head.next = Node(6)
linkedlist1.head.next.next = Node(9)

list1 = linkedlist.head
while list1:
    print(list1.data)
    list1 = list1.next
list2 = linkedlist1.head
while list2:
    print(list2.data)
    list2 = list2.next
    
list1 = linkedlist.head
list2 = linkedlist1.head

sortedlist = None

while list1 and list2:
    if list1 and list2 and list1.data <= list2.data:
        temp = list1.next
        list1.next = None
        if sortedlist:
            nodevalue = sortedlist
            while nodevalue.next:
                nodevalue = nodevalue.next
            print("inserted1",list1.data)
            nodevalue.next = list1
        else:
            sortedlist = list1
        
        list1 = temp
    elif list2:
        
        temp = list2.next
        list2.next = None
        if sortedlist:
            nodevalue = sortedlist
            while nodevalue.next:
                nodevalue = nodevalue.next
            print("inserted2",list2.data)
            nodevalue.next = list2
        else:
            sortedlist = list2
        list2 = temp
        
if list1:
    if sortedlist:
        nodevalue = sortedlist
        while nodevalue.next:
            nodevalue = nodevalue.next
        # print("inserted2",list1.data)
        nodevalue.next = list1
    else:
        sortedlist = list1

if list2:
    if sortedlist:
        nodevalue = sortedlist
        while nodevalue.next:
            nodevalue = nodevalue.next
        # print("inserted2",list2.data)
        nodevalue.next = list2
    else:
        sortedlist = list2




while sortedlist:
    print(sortedlist.data)
    sortedlist = sortedlist.next
    


# optimized 
nodes = Node(0)
tail = nodes

while list1 and list2:
    if list1.data< list2.data:
        tail.next = list1
        list1 = list1.next
    else:
        tail.next = list2
        list2 = list2.next
    tail = tail.next    
if list1:
    tail.next = list1
    
if list2:
    tail.next = list2
    
    
while nodes:
    print(nodes.data)
    nodes = nodes.next
    