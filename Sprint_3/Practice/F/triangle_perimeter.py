def count_perimeter():
    lines_count = int(input())
    lines = sorted(map(int, input().strip().split()))[::-1]

    perimeter = 0

    for i in range(lines_count - 2):
        if lines[i] < (lines[i + 1] + lines[i + 2]):
            perimeter = lines[i] + lines[i + 1] + lines[i + 2]
            break

    return perimeter


if __name__ == '__main__':
    print(count_perimeter())
