"""
-- ПРИНЦИП РАБОТЫ --
Алгоритм следующий: если дорога типа 'B' то добавлял путь как есть, если типа 'R', то инвертировал путь, после этого
вся задача свелась к нахождению цикла в графе.

Поиску цикла в графе был посвящен отдельный пункт в теории к спринту: "DFS. Поиск цикла и времена входа-выхода".

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение соответствует алгоритму, представленному в теории (речь об алгоритме обхода в глубину DFS) поэтому
на мой взгляд, мое решение корректно.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность DFS алгоритма O(V + E), где V - кол во вершин,
                                      E - кол-во ребер.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
## Дополнительная память используется для хранения графа O(V^2) - в худшем случае.

Без учета памяти под граф - для хранения списка вершин, посещенных вершин, стека и вершин,
которые в процессе обработки O(V).
"""

"""
-- ID успешной посылки --
63144954
"""

TYPE_BACKWARD = 'R'


def DFS(graph, n):
    verticies = range(n)

    visited = [False for _ in range(n)]

    stack = []

    on_stack = [False for _ in range(n)]

    for v in verticies:
        if visited[v]:
            continue

        stack.append(v)

        while stack:
            s = stack[-1]

            if not visited[s]:
                visited[s] = True
                on_stack[s] = True
            else:
                on_stack[s] = False
                stack.pop()
                continue

            for weight in graph[s]:
                if not visited[weight]:
                    stack.append(weight)
                elif on_stack[weight]:
                    return True

    return False


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n)]

    for i in range(n - 1):
        symbols_count = n - i - 1

        input_str = input().strip()

        railways = list(input_str)

        for j in range(i + 1, i + symbols_count + 1):
            symbol = railways[j - i - 1]
            if symbol == TYPE_BACKWARD:
                graph[i].append(j)
            else:
                graph[j].append(i)

    has_cycle = DFS(graph, n)

    print('NO' if has_cycle else 'YES')
