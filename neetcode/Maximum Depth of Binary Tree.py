

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)

# 
def maxdepth(root):
    if not root:
        return 0
    left = 1+ maxdepth(root.left)
    right = 1+ maxdepth(root.right)
    return max(left,right)

maxdepth(root)

def levelOrder(root):
    queue =[root]
    level = 0
    while queue:
        for i in queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level +=1
    return level

levelOrder(root)


