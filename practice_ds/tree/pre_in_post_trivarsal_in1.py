# This function combine all trivarsal in one.

#  It have time complexity of o(3n) because we need to traverse for all 3 traversal and space complexity is o(4n), 


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
        
def allTrivarsal(node):
    stack = []
    preorder , inorder , postorder = [],[],[]
    stack.append([node,1])
    if node ==None:
        return preorder,inorder,postorder 
    while True:
        if not stack:
            break
        # print(stack)
        if stack[-1][1] == 1:
            preorder.append(stack[-1][0].value)
            stack[-1][1] +=1
            if stack[-1][0].left != None:
                stack.append([stack[-1][0].left,1])
        elif stack[-1][1] == 2:
            inorder.append(stack[-1][0].value)
            stack[-1][1] +=1
            if stack[-1][0].right != None:
                stack.append([stack[-1][0].right,1])
        else:
            postorder.append(stack[-1][0].value)
            stack.pop()
        
    return preorder,inorder,postorder 


if __name__ == '__main__':
    ''' 
           1
         /   \
        2      3
     /    \    
   4       5     
         /   \
        6     7

   '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)
    preorder,inorder,postorder = allTrivarsal(root)

    print("Answer --------------->", preorder,inorder,postorder)
