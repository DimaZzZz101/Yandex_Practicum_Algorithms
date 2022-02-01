MODULE = 10 ** 9 + 7


def fib_mod(x):
    fibs = [0, 1] + [0] * (x - 1)

    for n in range(2, x + 1):
        fibs[n] = (fibs[n - 1] + fibs[n - 2]) % MODULE

    return fibs[x]


if __name__ == '__main__':
    x = int(input().strip())

    print(str(fib_mod(x + 1)))
