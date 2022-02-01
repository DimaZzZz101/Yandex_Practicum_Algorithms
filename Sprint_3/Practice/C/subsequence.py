def is_subsequence(str1, str2):
    if len(str1) == 0:
        return True
    if len(str2) == 0:
        return False

    index = 0
    current = str1[index]

    for letter in str2:
        if letter == current:
            index += 1
            if len(str1) == index:
                return True
            current = str1[index]
    return False


def main():
    str1 = input().strip()
    str2 = input().strip()

    print(is_subsequence(str1, str2))


if __name__ == '__main__':
    main()
