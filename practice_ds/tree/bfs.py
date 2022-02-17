
from unittest import result


class Node:
    def __init__(self,value):
        self.left =None
        self.right = None
        self.value = value
        
def levelorder(node):
    res = []
    if node.value == None:
        return res
    queue = []
    queue.append(node)
    while len(queue):
        for _ in range(len(queue)):
            queuenode = queue.pop(0)
            if queuenode.left:
                queue.append(queuenode.left)
            if queuenode.right:
                queue.append(queuenode.right)
            res.append(queuenode.value)
                
    return res
    
    


if __name__ =='__main__':
    ''' 
           1
         /   \
        2      3
     /    \    /  \
   4       5   6    7  
   
   
   '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.left.right = Node(9)
    root.right.left = Node(6)
    root.right.right = Node(17)
    levelorder(root)

