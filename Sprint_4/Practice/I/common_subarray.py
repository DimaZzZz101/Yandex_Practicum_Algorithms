def max_common_length(large, small):
    max_common_len = 0
    current_len = 0

    if large == small:
        return len(large)

    large_hash = {}

    for i, score in enumerate(large):
        if large_hash.get(score) is None:
            large_hash[score] = [i]
        else:
            large_hash[score].append(i)

    for i1, score in enumerate(small):
        if score not in large_hash:
            continue

        if len(small) - i1 <= max_common_len:
            break

        for i2 in large_hash.get(score):
            if len(large) - i2 <= max_common_len:
                break

            i = i1
            j = i2

            while i < len(small) and j < len(large) and small[i] == large[j]:
                current_len += 1
                i += 1
                j += 1

            max_common_len = max(max_common_len, current_len)
            current_len = 0

    return max_common_len


def main():
    n = int(input())
    first = input().split()

    m = int(input())
    second = input().split()

    print(max_common_length(first if n >= m else second, second if m <= n else first))


if __name__ == '__main__':
    main()
