# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root) -> int:
    return tree_depth(root)


def tree_depth(root) -> int:
    if root is None:
        return 0

    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1
