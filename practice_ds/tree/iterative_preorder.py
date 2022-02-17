# Iterative preorder , It follow the root, left, right

#  It have time complexity of o(n) and space complexity is o(n) , 
#  the worst space complexity is o(h), h is the height of the tree

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


def iterativePreorder(root):
    answer = []
    if root == None:
        return answer
    stack = []
    stack.append(root)
    while stack:
        for _ in stack:
            stacknode = stack.pop()

            if stacknode.right != None:
                stack.append(stacknode.right)

            if stacknode.left != None:
                stack.append(stacknode.left)
            answer.append(stacknode.value)

    return answer


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
    answer = iterativePreorder(root)

    print("Answer --------------->", answer)
