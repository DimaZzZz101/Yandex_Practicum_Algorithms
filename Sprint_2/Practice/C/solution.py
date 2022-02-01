from node import Node


def solution(node, elem) -> int:
    current_node = node
    index = 0

    while current_node is not None:
        if current_node.value == elem:
            return index

        if current_node.next_item is None:
            return -1

        current_node = current_node.next_item
        index += 1
