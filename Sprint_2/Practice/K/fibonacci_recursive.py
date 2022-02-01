def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    n = int(input())
    print(fibonacci_recursive(n))


if __name__ == '__main__':
    main()
