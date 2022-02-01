def find_golden_mean(sequence):
    mean = 0

    if len(sequence) == 0:
        return mean

    if len(sequence) == 1:
        return sequence[0]

    l = 0
    m = len(sequence) // 2
    r = len(sequence)

    mean = sequence[m] if (r - l) % 2 != 0 else (sequence[m] + sequence[m - 1]) / 2

    return mean


def main():
    n = int(input())
    k = int(input())

    northern_part = list(map(int, input().split()))[:n]
    southern_part = list(map(int, input().split()))[:k]

    print('{0:g}'.format(find_golden_mean(sorted(northern_part + southern_part))))


if __name__ == '__main__':
    main()
