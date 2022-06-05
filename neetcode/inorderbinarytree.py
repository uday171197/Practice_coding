


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# using recursion Approch
# preorder (Root,Left, Right)

def preOrder(root):
    if not root:
        return
    
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)


# inorder (Left,Root, Right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)


# postorder (Left,Root, Right)

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)
preOrder(root) 
inOrder(root)
postOrder(root)

#  Second Method

def preOrder(root):
    stack = []
    stack.append(root)
    while stack:
        newnode = stack.pop()
        if newnode.right:
            stack.append(newnode.right)
        if newnode.left:
            stack.append(newnode.left)
        print(newnode.data)


# inorder (Left,Root, Right)

def inOrder(root):
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            node = stack.pop()
            print(node.data)
            root = node.right


# postorder (Left,Root, Right)

def postOrder(root):
    stack1 = []
    stack2 = []
    stack1.append(root)
    while root and stack1:
        node = stack1.pop()
        stack2.append(node.data)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    return stack2[::-1]
        
        
        
preOrder(root) 
inOrder(root)
postOrder(root)
