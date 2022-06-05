
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

def inorder(root):
    if not root:
        return
    print(root.data)
    inorder(root.left)
    inorder(root.right)


inorder(root)

def invertTree(root):
    if not root:
        return None
    temp = root.right
    root.right = root.left
    root.left = temp
    invertTree(root.left)
    invertTree(root.right)
    return root
            
root1 = invertTree(root)


inorder(root1)
    

