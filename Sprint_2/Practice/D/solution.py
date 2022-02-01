from node import Node


def solution(node, idx) -> Node:
    if idx == 0:
        return node.next_item

    previous_node = None
    next_node = None
    current_node = node

    for i in range(idx):
        previous_node = current_node
        current_node = current_node.next_item
        if i == idx - 1:
            next_node = current_node.next_item if current_node is not None else None

    previous_node.next_item = next_node

    return node
