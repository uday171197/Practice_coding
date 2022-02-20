# Iterative postorder , It follow the  left, right,root

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
# method 1
def IterativePostorder(node):
    stack2 = []
    if node == None:
        return stack2
    stack1 = []
    stack1.append(node)
    
    while stack1:
        node = stack1.pop()
        stack2.append(node.value)
        if node.left != None:
            stack1.append(node.left)
        if node.right != None:
            stack1.append(node.right)
                
    return stack2[::-1]

#method 2:  it have time complexity of o(2n) because we are using first loop to traverse left ofter that
# we are using another loop for to fetch right traversal thah make o(n+n) = o(2n)
def IterativePostordermethod2(node):
    stack = []
    ans = []
    while node != None or stack:
       
        if node != None:
            stack.append(node)
            node = node.left
        else:
            temp = stack[-1].right
            if temp == None:
                temp = stack.pop()
                ans.append(temp.value)
                while stack and stack[-1].right == temp:
                    temp = stack.pop()
                    ans.append(temp.value)
            else:
                node = temp
                
    return ans


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
    answer = IterativePostorder(root)
    print("Answer --------------->", answer)
    
    answer = IterativePostordermethod2(root)
    print("Answer --------------->", answer)
