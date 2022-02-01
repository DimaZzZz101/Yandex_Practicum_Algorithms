# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def tree_len(Node):
    if Node.left is None and Node.right is None:
        return 1

    left_len = 0
    if Node.left is not None:
        left_len = tree_len(Node.left)

    right_len = 0
    if Node.right is not None:
        right_len = tree_len(Node.right)

    return 1 + max(left_len, right_len)


def solution(Node) -> bool:
    balanced = True

    if Node is None:
        return balanced

    if (Node.left is None) and (Node.right is None):
        return balanced

    left_len = 0
    if Node.left is not None:
        left_len = tree_len(Node.left)

    right_len = 0
    if Node.right is not None:
        right_len = tree_len(Node.right)

    diff = left_len - right_len

    if abs(diff) <= 1 and solution(Node.right) is True and solution(Node.left) is True:
        return True

    return False
