# Iterative preorder , It follow the  left,root, right

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
        
def Maxsum(node,maxvalue):
    if node == None:
        return 0,maxvalue
    
    leftsum,maxvalue = Maxsum(node.left,maxvalue)
    rightsum,maxvalue = Maxsum(node.right,maxvalue)
    
    maxvalue = max(maxvalue,leftsum + rightsum + node.value)
    return node.value + max(leftsum ,rightsum),maxvalue
    


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
    root.left.right = Node(-5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)
    answer,maxsum = Maxsum(root,0)

    print("maxsum --------------->", maxsum)
