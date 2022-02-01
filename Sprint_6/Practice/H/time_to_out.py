COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'


def dfs_stack(start, graph, colors, entry, out):
    stack = [start]
    time = -1

    while len(stack) > 0:
        v = stack.pop()

        if colors[v] == COLOR_WHITE:
            time += 1
            entry[v] = time

            colors[v] = COLOR_GRAY
            stack.append(v)

            for node in sorted(graph.get(v))[::-1]:
                if colors[node] == COLOR_WHITE:
                    stack.append(node)
        elif colors[v] == COLOR_GRAY:
            colors[v] = COLOR_BLACK
            time += 1
            out[v] = time


if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}

    colors = [COLOR_WHITE for n in range(n + 1)]
    entry = [0 for n in range(n + 1)]
    leave = [0 for n in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().strip().split())
        adjacency_list.get(u).append(v)

    start = 1

    dfs_stack(start, adjacency_list, colors, entry, leave)

    for i in range(1, n + 1):
        print(f"{entry[i]} {leave[i]}")
