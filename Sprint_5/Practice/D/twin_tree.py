# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def is_equal(left_root, right_root) -> bool:
    if left_root is None and right_root is None:
        return True

    if (type(left_root) != type(right_root)) or (left_root.value != right_root.value):
        return False

    return is_equal(left_root.left, right_root.left) and is_equal(left_root.right, right_root.right)


def solution(root1, root2) -> bool:
    return is_equal(root1, root2)
