def neighbors(matrix, y, x):
    neighbors_list = []
    if x + 1 < len(matrix[0]):
        neighbors_list.append(matrix[y][x + 1])
    if x - 1 >= 0:
        neighbors_list.append(matrix[y][x - 1])
    if y + 1 < len(matrix):
        neighbors_list.append(matrix[y + 1][x])
    if y - 1 >= 0:
        neighbors_list.append(matrix[y - 1][x])

    return neighbors_list


if __name__ == "__main__":
    n = int(input())  # Строки матрицы
    m = int(input())  # Столбцы матрицы

    matrix = [list(map(int, input().split())) for i in range(n)]

    y = int(input())
    x = int(input())

    print(*sorted(neighbors(matrix, y, x)))
