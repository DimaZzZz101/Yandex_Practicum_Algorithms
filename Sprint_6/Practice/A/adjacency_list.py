def main():
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}

    for _ in range(m):
        u, v = map(int, input().strip().split())
        adjacency_list.get(u).append(v)

    for item in adjacency_list.values():
        print(f"{len(item)} {' '.join(map(str, sorted(item)))}")


if __name__ == '__main__':
    main()
