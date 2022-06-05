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
linkedlist.head.next.next = Node(3)
node = linkedlist.head
while node != None:
    print(node.data)
    node = node.next

previous = None
curr = linkedlist.head

while curr:
    temp = curr.next
    print(curr.data)
    curr.next = previous
    previous = curr
    curr = temp
    
while previous:
    print(previous.data)
    previous = previous.next
    

node = linkedlist.head
while node != None:
    print(node.data)
    node = node.next
    
def reverseLinkedList(head):
    if not head:
        return None
    
    newhead = head
    if head.next:
        newhead = reverseLinkedList(head.next)
        head.next.next = head
    head.next = None
    
    return newhead

previous = reverseLinkedList(linkedlist.head)
while previous:
    print(previous.data)
    previous = previous.next
    

        

