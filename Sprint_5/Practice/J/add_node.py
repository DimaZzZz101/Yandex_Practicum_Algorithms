from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def insert(root, key):
    if root is None:
        root = Node(value=key)
        return root

    if key < root.value:
        if root.left is not None:
            insert(root.left, key)
        else:
            root.left = Node(value=key)

    elif key >= root.value:
        if root.right is not None:
            insert(root.right, key)
        else:
            root.right = Node(value=key)

    return root
