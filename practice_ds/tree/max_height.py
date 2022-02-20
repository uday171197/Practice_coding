# This is used to find the maximum depth of the binary tree

#  It have time complexity of o(n) and space complexity is o(n) , 


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
# method 1
def MaxHeight(node):
    if node == None:
        return 0
    lh = MaxHeight(node.left)
    rh = MaxHeight(node.right)
    
    return 1+ max(lh,rh)

def MaxHeightLevelOrder(node):
    stack = []
    if node == None:
        return stack
    length = 1
    stack.append(node)
    while stack:
        for _ in stack:
            stack_node = stack.pop()
            if stack_node.left != None:
                stack.append(stack_node.left)
                
            if stack_node.right != None:
                stack.append(stack_node.right)
        length +=1
    return length
    
    
    
if __name__ == '__main__':
    ''' 
           1
         /   \
        2      3
     /    \    
   4       5     
         /   \
        6     7
                \ 
                 8
                  \
                  9
   469875231
   '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)
    root.left.right.right.right = Node(8)
    root.left.right.right.right.right = Node(9)
    answer = MaxHeight(root)
    print("Max height --------------->", answer)
    
    answer = MaxHeightLevelOrder(root)
    print("Max height --------------->", answer)
    
