def main():
    n, m = map(int, input().strip().split())

    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().strip().split())
        adjacency_matrix[u - 1][v - 1] = 1

    for line in adjacency_matrix:
        print(' '.join(map(str, line)))


if __name__ == '__main__':
    main()
