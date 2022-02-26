# Iterative preorder , It follow the  left,root, right

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

from httpx import ReadTimeout


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
#method 1
def preorder(node,ans):
    if node == None:
        return ans
    ans.append(node.value)
    preorder(node.left,ans)
    preorder(node.right,ans)
    return ans
    
# method 2
def identical(node1,node2):
    if node1 == None or node2 == None:
        return node1 == node2
    return (node1.value == node2.value)\
        and identical(node1.left,node2.left)\
        and identical(node1.right,node2.right)

    


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
    
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.right.left = Node(6)
    root1.left.right.right = Node(7)
    
    # it have o(3n) time complexity
    #method1
    tree1 = preorder(root,[])
    tree2 = preorder(root1,[])
    if tree1 == tree2:
        print('Identical')
    else:
        print('Not Identical')
    
    #method2
    result = identical(root,root1)
    
    if result:
        print('Identical')
    else:
        print('Not Identical')
        
    

