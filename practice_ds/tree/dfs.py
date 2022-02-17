
from unittest import result


class Node:
    def __init__(self,value):
        self.left =None
        self.right = None
        self.value = value
        



def preorder(node,result):
    """Preorder Traversal root, left, right

    Args:
        node (node): root node
    """    
    if node == None:
        return
    # print(node.value)
    result.append(node.value)
    preorder(node.left,result)
    preorder(node.right,result)
    return result
    


def inorder(node,result):
    """Inorder Traversal left,root, right
        time complexity for this is o(n) , n is the no of node and o(n)
        is because we need to traverse to each node.
        
        The space complexity for this is o(n), because we have to go to length of node.
        
         
    Args:
        node (node): root node
    """  
    if node == None:
        return
    inorder(node.left,result)
    # print(node.value)
    result.append(node.value)
    inorder(node.right,result)
    return result
    


def postorder(node,result):
    """Postorder Traversal left,right,root

    Args:
        node (node): root node
    """  
    if node == None:
        return
    postorder(node.left,result)
    postorder(node.right,result)
    # print(node.value)
    result.append(node.value)
    return result
    


if __name__ =='__main__':
    ''' 
           1
         /   \
        2      3
     /    \    /  \
   4       5   6    7  
   
   
   '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    preorderresult = preorder(root,[])
    print('preorderresult ----------->',preorderresult)
    inorderresult = inorder(root,[])
    print('inorderresult ----------->',inorderresult)
    postorderresult = postorder(root,[])
    print('postorderresult ----------->',postorderresult)