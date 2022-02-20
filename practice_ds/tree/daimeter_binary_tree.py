# Iterative postorder , It follow the  left, right,root

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

def daimeter(node,maxlength):
    if node == None:
        return 0
    lh = daimeter(node.left,maxlength)
    rh = daimeter(node.right,maxlength)
    maxlength = max((lh + rh),maxlength)
    print(lh,rh,maxlength)
    return 1+ max(lh,rh)


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
   
   '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.left.left = Node(6)
    root.right.right.right = Node(7)
    root.right.left.left.left = Node(8)
    root.right.right.right.right = Node(9)
    
    answer = daimeter(root,0)
    print("Answer --------------->", answer)
