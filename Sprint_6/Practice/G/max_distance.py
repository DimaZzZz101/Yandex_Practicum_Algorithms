from collections import deque

COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'


def bfs(start, graph, colors, distance):
    planned = deque([start])
    previous = {}
    colors[start] = COLOR_GRAY

    while len(planned) > 0:
        u = planned.pop()
        for v in sorted(graph.get(u)):
            if colors[v] == COLOR_WHITE:
                distance[v] = distance[u] + 1
                previous[v] = u
                colors[v] = COLOR_GRAY
                planned.appendleft(v)

        colors[u] = COLOR_BLACK


if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}
    colors = {(n + 1): COLOR_WHITE for n in range(n)}

    for _ in range(m):
        u, v = map(int, input().strip().split())

        adjacency_list.get(u).append(v)
        adjacency_list.get(v).append(u)

    start = int(input().strip())

    distance = {start: 0}
    bfs(start, adjacency_list, colors, distance)

    print(str(max(distance.values())))
