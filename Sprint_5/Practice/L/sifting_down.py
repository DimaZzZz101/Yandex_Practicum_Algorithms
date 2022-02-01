def sift_down(heap, index) -> int:
    left_index = 2 * index
    right_index = 2 * index + 1
    heap_size = (len(heap) - 1)

    if heap_size < left_index:
        return index

    if right_index <= heap_size and heap[left_index] < heap[right_index]:
        index_largest = right_index
    else:
        index_largest = left_index

    if heap[index] < heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        index = sift_down(heap, index_largest)

    return index
