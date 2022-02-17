'''
A binary tree is a data structure in which every node or vertex has atmost two children. 
In Python, a binary tree can be represented in different ways with different data 
structures(dictionary, list) and class representation for a node.
However, binarytree library helps to directly implement a binary tree. 
It also supports heap and binary search tree(BST).
'''
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
''' following is the tree after above statement
        1
      /   \
     None  None'''
     

root = Node(1)
root.value

''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   None None None None'''
root.left = Node(2)
root.right = Node(3)

print(root.left.value,root.value,root.right.value)

'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''

root.left.left = Node(4)
print(root.left.left.value)
