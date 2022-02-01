def sift_up(heap, index) -> int:
    if index == 1:
        return index

    parent_idx = index // 2

    if heap[parent_idx] < heap[index]:
        heap[index], heap[parent_idx] = heap[parent_idx], heap[index]
        index = sift_up(heap, parent_idx)

    return index
