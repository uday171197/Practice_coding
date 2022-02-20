# balance tree, if diff between left node height and right node height is less then and equal to 1.

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
        
def balanceTree(node):
    if node == None:
        return 0
    
    l = balanceTree(node.left)
    if l == -1:
        return -1
    r = balanceTree(node.right)
    if r == -1 :
        return -1
    
    if abs(l-r) > 1:
        return -1
    
    return max(l,r)+1


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
    answer = balanceTree(root)
    if answer == -1:
        print("Not a balance tree")
    else:
        print("Is a balance tree")
