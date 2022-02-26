# Iterative preorder , It follow the  left,root, right

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
        
def ZigZag(node):
    ans = []
    if node == None:
        return ans
    queue = []
    flag = 0
    queue.append(node)
    while queue:
        levelnode = []
        for _ in range(len(queue)):
            stacknode = queue.pop(0)
            if stacknode.left != None:
                queue.append(stacknode.left)
            if stacknode.right != None:
                queue.append(stacknode.right)
            print(stacknode.value)
            levelnode.append(stacknode.value)
        
        if flag:
            ans.extend(levelnode[::-1])
            flag = 0
        else:
            ans.extend(levelnode)
            flag = 1
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
    answer = ZigZag(root)

    print("ZigZag --------------->", answer)
