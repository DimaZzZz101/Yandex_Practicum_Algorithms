# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left

def print_range(root, left: int, right: int) -> None:
    if root is None:
        return

    if left <= root.value:
        print_range(root.left, left, right)

    if left <= root.value <= right:
        print(root.value)

    if right >= root.value:
        print_range(root.right, left, right)