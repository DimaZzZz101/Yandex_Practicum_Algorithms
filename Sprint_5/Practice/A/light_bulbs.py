# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(Node) -> int:
    root_value = Node.value

    if (Node.left is None) and (Node.right is None):
        return root_value

    if Node.left is not None:
        left_value = solution(Node.left)
    else:
        left_value = 0

    if Node.right is not None:
        right_value = solution(Node.right)
    else:
        right_value = 0

    return max(root_value, left_value, right_value)
