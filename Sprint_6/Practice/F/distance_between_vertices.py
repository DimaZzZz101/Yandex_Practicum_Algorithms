from collections import deque

COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'

DISTANCE_INF = -1


def bfs(start, graph, colors, distance, finish):
    if start == finish:
        return distance[start]

    planned = deque([start])
    previous = {}
    colors[start] = COLOR_GRAY

    while len(planned) > 0:
        u = planned.pop()
        
        for v in graph.get(u):
            if colors[v] == COLOR_WHITE:
                distance[v] = distance[u] + 1
                previous[v] = u
                colors[v] = COLOR_GRAY
                planned.appendleft(v)

                if v == finish:
                    return distance[v]

        colors[u] = COLOR_BLACK

    return DISTANCE_INF


if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}

    colors = [COLOR_WHITE for n in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().strip().split())
        adjacency_list.get(u).append(v)
        adjacency_list.get(v).append(u)

    s, t = map(int, input().strip().split())

    distance = {s: 0}

    print(str(bfs(s, adjacency_list, colors, distance, t)))
