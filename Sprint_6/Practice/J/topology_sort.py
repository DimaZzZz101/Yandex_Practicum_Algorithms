COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'


def topology_sort(v, graph, colors, dag):
    colors[v] = COLOR_GRAY

    for node in graph.get(v):
        if colors[node] == COLOR_WHITE:
            topology_sort(node, graph, colors, dag)

    colors[v] = COLOR_BLACK
    dag.append(v)


if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}
    colors = [COLOR_WHITE for n in range(n + 1)]
    order = [(0, 0) for m in range(m)]

    for i in range(m):
        u, v = map(int, input().strip().split())
        adjacency_list.get(u).append(v)
        order[i] = (u, v)

    dag = []

    for u, _ in order:
        if colors[u] == COLOR_WHITE:
            topology_sort(u, adjacency_list, colors, dag)

    for i in range(1, n + 1)[::-1]:
        if colors[i] == COLOR_WHITE:
            topology_sort(i, adjacency_list, colors, dag)

    print(' '.join(map(str, reversed(dag))))
