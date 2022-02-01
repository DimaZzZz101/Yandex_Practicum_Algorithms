COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'


def dfs_stack(start, graph, colors, path):
    stack = [start]

    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == COLOR_WHITE:
            colors[v] = COLOR_GRAY
            stack.append(v)
            path.append(v)

            for node in reversed(sorted(graph.get(v))):
                if colors[node] == COLOR_WHITE:
                    stack.append(node)
        elif colors[v] == COLOR_GRAY:
            colors[v] = COLOR_BLACK


def main():
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}

    colors = {(n + 1): COLOR_WHITE for n in range(n)}

    for _ in range(m):
        u, v = map(int, input().strip().split())
        adjacency_list.get(u).append(v)
        adjacency_list.get(v).append(u)

    start = int(input().strip())

    path = []

    dfs_stack(start, adjacency_list, colors, path)

    print(' '.join(map(str, path)))


if __name__ == '__main__':
    main()
