# Iterative preorder , It follow the  left,root, right

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
        
def preorder(node,ans):
    if node == None:
        return ans
    ans.append(node.value)
    preorder(node.left,ans)
    preorder(node.right,ans)
    return ans
        
def boundrytree(node):
    ans = []
    if node == None:
        return ans
    ans.append(node.value)
    leftnodevalue = preorder(node.left,[])
    rightnodevalue = preorder(node.right,[])
    ans.extend(leftnodevalue)
    ans.extend(rightnodevalue[::-1])
    return ans
            
    
    


if __name__ == '__main__':
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
    answer = boundrytree(root)

    print("boundry --------------->", answer)
