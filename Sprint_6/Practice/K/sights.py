import math

DISTANCE_INF = -1


def dejkstra(start, graph, distances):
    distance = [math.inf for _ in range(len(graph) + 1)]
    parent = [None for _ in range(len(graph) + 1)]
    visited = [False for _ in range(len(graph) + 1)]

    distance[start] = 0

    while True:
        u = get_min_dist_to_not_visited(graph, visited, distance)

        if u is None:
            return

        visited[u] = True
        distances[u - 1][u - 1] = 0
        for v in [v[0] + 1 for v in enumerate(graph[u - 1]) if v[1] < math.inf]:
            relax(start, u, v, graph, distance, parent, distances)


def get_min_dist_to_not_visited(graph, visited, distance):
    current_minimum = math.inf
    current_minimum_vertex = None

    for v in range(1, len(graph) + 1):
        if not visited[v] and distance[v] < current_minimum:
            current_minimum = distance[v]
            current_minimum_vertex = v

    return current_minimum_vertex


def relax(start, u, v, graph, distance, parent, distances):
    if parent[u] == v:
        return

    distance_u_v = distance[u] + graph[u - 1][v - 1]

    if distance[v] > distance_u_v:
        distance[v] = distance_u_v
        parent[v] = u

        distances[start - 1][v - 1] = distance[v]
        distances[v - 1][start - 1] = distance[v]


if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    adjacency_matrix = [[math.inf for _ in range(n)] for _ in range(n)]

    distance_matrix = [[DISTANCE_INF for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().strip().split())

        if adjacency_matrix[u - 1][v - 1] > w:
            adjacency_matrix[u - 1][v - 1] = w
            adjacency_matrix[v - 1][u - 1] = w

    for node in range(1, n + 1):
        dejkstra(node, adjacency_matrix, distance_matrix)

    for line in distance_matrix:
        print(' '.join(map(str, line)))