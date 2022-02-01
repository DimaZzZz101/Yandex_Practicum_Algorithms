def find_all(search, pattern):
    occurrences = []

    len_pattern = len(pattern)
    len_search = len(search)

    if len_pattern > len_search:
        return occurrences

    start = 0

    while True:
        pos = find(search, pattern, start)
        if pos == -1:
            break
        occurrences.append(pos)
        start = pos

    return occurrences


def find(search, pattern, start):
    result = -1

    if start >= len(search):
        return result

    if len(search) - start < len(pattern):
        return result

    for pos in range(start, len(search) - len(pattern) + 1):
        shift = None
        match = True

        for offset in range(len(pattern)):
            if shift is None:
                shift = pattern[offset] - search[pos]

            if search[pos + offset] + shift != pattern[offset]:
                match = False
                break

        if match:
            result = pos + 1
            break

    return result


if __name__ == '__main__':
    n = int(input().strip())
    search = list(map(int, input().strip().split()[:n]))

    m = int(input().strip())
    pattern = list(map(int, input().strip().split()[:m]))

    print(' '.join(map(str, find_all(search, pattern))))
