import sys

"""
-- ПРИНЦИП РАБОТЫ --
Из входных данных формируется куча (бинарное дерево). Далее происходит вставка с помощью алгоритма просеивания
вверх. Учитывая компаратор, восстанавливаем свойства кучи. После того, как все элементы были добавлены в кучу,
мы извлекаем их в упорядоченном порядке в итоговый массив. На каждой такой итерации выполняется просевание вниз =>
свойства кучи восстанавливаются.

# Примечание: функции просеивания были реализованы ранее в контесте

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Алгоритм корректен, так как куча представляет собой приоритетную очередь (из определения),
а приоритет высчитывается c помощью компаратора.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Пирамидальная сортировка в худшем случае покажет результат O(n*log(n)), где n - кол-во элеметов в заданном массиве.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Так как выделяется память под массив, в котором храним все элементы кучи, то сложность будет O(N).
"""

"""
-- ID успешной посылки --
60626282
"""


"""
Возник вопрос: я не совсем понял, касательно реализации in place,
можно, пожалуйста, дополнителью подсказку или объяснить по подробнее?
"""


# Просеивание вверх.
def sift_up(heap, index) -> int:
    if index == 0:
        return index

    parent_index = (index - 1) // 2

    if heap[parent_index] > heap[index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]

        index = sift_up(heap, parent_index)

    return index


# Просеивание вниз
def sift_down(heap, index) -> int:
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    heap_size = len(heap) - 1

    # Случай, когда дочерних элементов нет.
    if heap_size < left_index:
        return index

    # Случай, когда два дочерних элемента.
    if right_index <= heap_size and heap[left_index] > heap[right_index]:
        index_largest = right_index
    else:
        index_largest = left_index

    if heap[index] > heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]

        index = sift_down(heap, index_largest)

    return index


if __name__ == '__main__':
    n = int(input())

    participants: list = []

    for i in range(0, n):
        # Формируем кортеж из вводимых данных: (логин, число решенных задач, штраф)
        login, completed, penalty = sys.stdin.readline().strip().split()

        participants.append((-int(completed), int(penalty), login))

        sift_up(participants, i)

    for i in range(n, 0, -1):
        print(participants[0][2])

        if i > 1:
            participants[0] = participants.pop()

        sift_down(participants, 0)
