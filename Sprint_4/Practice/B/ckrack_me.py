from string import ascii_lowercase
from random import choices


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
    a = 1000
    m = 123987123

    hashes = {}

    i = 0

    while True:
        check = ''.join(choices(ascii_lowercase, k=10))
        hashed = polynomial_hash(check, a, m)

        if hashes.get(hashed) is not None:
            hashes[hashed].append(check)
            print(f'{check} {hashes[hashed]}')
        else:
            hashes[hashed] = [check]

        i += 1

        if i % 100000000 == 0:
            print(f'{i} Checks')


if __name__ == '__main__':
    main()
