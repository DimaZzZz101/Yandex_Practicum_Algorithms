import string


def compare(first, second):
    if first < second:
        return '-1'
    elif first > second:
        return '1'
    else:
        return '0'


if __name__ == "__main__":
    ALPHABET = set(list(string.ascii_lowercase)[1::2])

    first = ''.join(filter(lambda char: char in ALPHABET, list(input().strip())))
    second = ''.join(filter(lambda char: char in ALPHABET, list(input().strip())))

    print(compare(first, second))
