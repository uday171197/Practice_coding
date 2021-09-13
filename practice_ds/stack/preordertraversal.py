class node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data
      
root = node(10)
root.left = node(3)
root.right = node(5)
root.right.right = node(9)
root.left.left = node(4)
root.right.left = node(6)

def main(root):
    if root is None:
        return
    a = []
    a.append(root)
    while len(a)>0:
        print('lenght',len(a))
        nodes = a.pop()
        print(nodes.data)
       
        if nodes.right is not None:
            a.append(nodes.right)
        if nodes.left is not None:
            a.append(nodes.left)
        
main(root)
        
        
