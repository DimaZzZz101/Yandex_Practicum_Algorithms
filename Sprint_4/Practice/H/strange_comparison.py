from string import ascii_lowercase


def comparator(check, match):
    if not set(check).issubset(ascii_lowercase) or not set(match).issubset(ascii_lowercase):
        return False

    if len(check) != len(match):
        return False

    chars = {}
    used = {}

    for i, char in enumerate(match):
        if chars.get(char) is None and check[i] not in used:
            chars[char] = check[i]
            used[check[i]] = True
        elif chars.get(char) == check[i]:
            continue
        else:
            return False

    return True


def main():
    one = input()
    two = input()

    print('YES' if comparator(one, two) else 'NO')


if __name__ == '__main__':
    main()
