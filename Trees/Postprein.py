class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
def printPreorder(root):
 
    if root:
        print(root.val,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)
def printPostorder(root):
 
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end=" ")
        
def printInorder(root):
 
    if root:
        printInorder(root.left)
        print(root.val,end=" ")
        printInorder(root.right)
        

        
root = Node(1)
root.right     = Node(2)
root.right.right=Node(5)
root.right.right.left=Node(3)
root.right.right.right= Node(6)
root.right.right.left.right= Node(4)
printPreorder(root)
print("\n")
printPostorder(root)
print("\n")
printInorder(root)