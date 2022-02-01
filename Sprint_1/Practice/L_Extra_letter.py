def find_extra_letter(str1, str2):
    for char in str1:
        if char in str2:
            str2.remove(char)

    return str2


if __name__ == "__main__":
    base_string = list(input())
    string_with_extra_letter = list(input())

    print(*find_extra_letter(base_string, string_with_extra_letter))
