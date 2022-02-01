def fibonacci_recursive(n, k):
    if n == 0 or n == 1:
        return 1

    prev1 = 1
    prev2 = 1

    for _ in range(2, n):
        prev1, prev2 = prev2, (prev1 + prev2) % (10 ** k)

    return (prev1 + prev2) % (10 ** k)


def main():
    n, k = map(int, input().strip().split())
    print(fibonacci_recursive(n, k))


if __name__ == '__main__':
    main()
