def main():
    m = int(input().strip())
    n = int(input().strip())

    heaps = list(None for _ in range(n))

    for i in range(n):
        cost, mass = map(int, input().strip().split())
        heaps[i] = (cost, mass)

    value = 0

    for heap in sorted(heaps, reverse=True):
        volume = heap[1] if heap[1] <= m else m
        m -= volume
        value += heap[0] * volume

        if m == 0:
            break

    print(str(value))


if __name__ == '__main__':
    main()
