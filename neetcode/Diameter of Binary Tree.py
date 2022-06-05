class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)


def daimeter(root,maxvalue):
    if not root:
        return 0,maxvalue
    
    left,maxvalue = daimeter(root.left,maxvalue)
    right,maxvalue = daimeter(root.right,maxvalue)
    maxvalue = max((left+right),maxvalue)
    return 1 + max(left,right),maxvalue

daimeter(root,0)