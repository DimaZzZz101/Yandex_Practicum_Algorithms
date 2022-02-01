def polynomial_hash(string, a, m):
    result = 0
    length = len(string)

    if length == 0:
        return result

    if length == 1:
        return ord(string[0]) % m

    result = (ord(string[0]) * a + ord(string[1])) % m

    for i in range(2, len(string)):
        result = (result * a + ord(string[i])) % m

    return result


def main():
    a = int(input())
    m = int(input())
    s = input().strip()

    return polynomial_hash(s, a, m)


if __name__ == '__main__':
    print(main())
