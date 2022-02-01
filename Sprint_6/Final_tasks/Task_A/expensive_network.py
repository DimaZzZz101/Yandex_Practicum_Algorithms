from heapq import heappush, heappop

"""
-- ПРИНЦИП РАБОТЫ --
В данной задаче мы реализуем и немного модифицируем алгоритм Прима для поиска минимального остовного дерева (сам 
алгоритм был очень хорошо описан в теории к спринту). Собственно вместо минимума среди множества ребер остова,
мы ищем максимум, в итоге получаем максимально возможный вес остова, что т требуется по заданию.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Мое решение корректно, так как почти полностью реализовано по известному алгоритму Прима, который, как я писал выше
подробно описан в теории к спринту (см. раздел Спринт 6: Минимальное остовное дерево).
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Поскольку для поиска мы используем очередь с приоритетом, то сложность в основном будет зависеть от вида графа,
так в плотном графе E стремиться к V^2, в итоге получается,
что сложность будет O(E * log(V)), где V - кол во вершин,
                                       E - кол-во ребер.
Для плотных графов O(V^2) , так как V^2 -> E * log(V).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Так как мы храним пары вершин и ребра (w,v,u), то в результате пространственная сложность будет:
    O(V + E), где V - кол во вершин,
                  E - кол-во ребер.
"""

"""
-- ID успешной посылки --
63267405
"""


# Поиск МОД - минимального остовного дерева.
def find_mst(graph, edges, mst):
    not_added = {v for v in range(1, len(graph) + 1)}

    start = 1
    add_vertex(start, graph, not_added, edges)

    while not_added and edges:
        e = heappop(edges)

        if e[2] in not_added:
            mst += -e[0]
            add_vertex(e[2], graph, not_added, edges)

    if len(not_added) > 0:
        raise ValueError('Oops! I did it again')

    return mst


# Добавление вершин.
def add_vertex(v, graph, not_added, edges):
    not_added.remove(v)

    # Вершины представлены в виде tuple (w, v, u), очередь с приоритетом реализует min-heap-sort,
    # поэтому - веса отрицательные.
    for edge in [(-item[1], v, item[0]) for item in graph.get(v).items() if item[0] in not_added]:
        heappush(edges, edge)


if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    edges_list = {(n + 1): {} for n in range(n)}

    for _ in range(m):
        v, u, w = map(int, input().strip().split())

        if v == u:
            continue

        if edges_list.get(u).get(v) is None or edges_list[u].get(v) < w:
            edges_list[v][u] = w
            edges_list[u][v] = w

    mst = 0
    edges = []

    try:
        if n > 1 and m == 0:
            raise ValueError('Oops! I did it again')

        print(find_mst(edges_list, edges, mst))
    except ValueError as e:
        print(e)
