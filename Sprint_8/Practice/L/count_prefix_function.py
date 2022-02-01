def prefix_function(strng):
    prefix = [0] * len(strng)
    j = 0
    i = 1

    while i < len(strng):
        if strng[j] != strng[i]:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
        else:
            prefix[i] = j + 1
            i += 1
            j += 1

    return prefix


if __name__ == "__main__":
    string = input().strip()

    print(' '.join(map(str, prefix_function(string))))
