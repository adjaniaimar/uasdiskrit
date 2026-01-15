# DEFINISI NODE POHON BINER
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# POHON BINER
root = Node ('A')
root.left = Node ('B')
root.right = Node ('C')

root.left.left = Node ('D')
root.left.right = Node ('E')

root.right.right = Node ('F')

# TRAVERSAL POHON BINER
## PREORDER TRAVERSAL
def preorder(node):
    if node:
        print(node.data, end= '')
        preorder(node.left)
        preorder(node.right)

print("Preorder Travesal:")
preorder(root)

## INORDER TRAVESAL
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end= '')
        inorder(node.right)

print("Inorder Travesal:")
inorder(root)

## POSTORDER TRAVESAL
def postorder(node):
    if node:
        postorder(node.left)
        porstorder(node.right)
        print(node.data, end= '')

print("Postorder Travesal:")
postorder(root)