def get_partitions(seq):
    parts = []

    if len(seq) == 0:
        return parts

    if len(seq) == 1:
        parts.append(seq)
        return parts

    current = seq.copy()
    size = 1

    while len(current) > 0:
        while size <= len(current):
            if size == len(current):
                parts.append(current)
                current = []
                break

            block = current[:size]

            if max(block) > min(current[size:]):
                size += 1
                continue

            parts.append(block)
            current = current[size:]
            size = 1

    return parts


def main():
    n = int(input())
    sequence = list(map(int, input().strip().split()))[:n]

    print(len(get_partitions(sequence)))


if __name__ == '__main__':
    main()
