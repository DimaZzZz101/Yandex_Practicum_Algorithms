# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left
from collections import deque

sm = 0


def is_leaf(node):
    return node.left is None and node.right is None


def print_root_to_leaf_paths(node, path):
    if node is None:
        return

    path.append(node.value)

    global sm
    if is_leaf(node):
        res = int(''.join(map(str, list(path))))
        sm += res

    print_root_to_leaf_paths(node.left, path)
    print_root_to_leaf_paths(node.right, path)

    path.pop()


def solution(root) -> int:
    path = deque()
    print_root_to_leaf_paths(root, path)

    return sm
