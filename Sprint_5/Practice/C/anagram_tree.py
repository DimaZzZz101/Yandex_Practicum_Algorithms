# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def is_symmetric(root_left, root_right) -> bool:
    if root_left is None and root_right is None:
        return True

    if (type(root_left) != type(root_right)) or (root_left.value != root_right.value):
        return False

    return is_symmetric(root_left.left, root_right.right) and is_symmetric(root_left.right, root_right.left)


def solution(Node) -> bool:
    symmetric = True

    if Node is None:
        return symmetric

    return is_symmetric(Node, Node)
