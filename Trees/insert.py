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

def Insert(root,n):
    temp=root
    new_node=n
    if temp.value>=new_node.value:
        if temp.left is not None:
            Insert(temp.left,new_node)
        else:
            temp.left=new_node           
    else:
        if temp.right is not None:
            Insert(temp.right,new_node)
        else:
            temp.right=new_node

def Minimum(root):
    temp=root
    if temp.left is not None:
        Minimum(temp.left)
    else:
        return temp

def Successor(root,x)
     temp=root
     if x.right is not None:
        return Minimum(x.right)
     else:
        y=x.p
        z=y.p
        if(y.right==n):
            while y.p is not None:
                y=y.p
            return y
        else:
            if(z.left==y):
                return y
            else:
                while ((z.p is not None)and (z.right==y) and (z>x)):
                    y=z.p
                    z=z.p
                return y



        

        
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