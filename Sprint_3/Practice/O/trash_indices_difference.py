def trash_index(squares, k):
    if len(squares) == 2:
        return abs(squares[0] - squares[-1])

    left = 0
    right = squares[-1] - squares[0]
    mid = (left + right) // 2

    while right > left:
        i = 1
        prev = 0
        count = 0

        while i < len(squares) and prev < len(squares):
            if prev > i:
                break

            diff = squares[i] - squares[prev]

            if diff > mid:
                prev += 1
                continue

            count += (i - prev)
            i += 1

            if count >= k:
                break
        if count >= k:
            left = left
            right = mid
        else:
            left = mid + 1
            right = right

        mid = (left + right) // 2

    return left


def main():
    n = int(input())
    sequence = list(map(int, input().strip().split()))[:n]
    k = int(input())

    print(trash_index(sorted(sequence), k))


if __name__ == '__main__':
    main()
