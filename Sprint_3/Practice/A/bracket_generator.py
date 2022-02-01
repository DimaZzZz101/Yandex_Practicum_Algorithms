def bracket_generator(length, result, opened=0, closed=0, line=''):
    if opened + closed == 2 * length:
        result.append(line)
        return
    else:
        if opened < length:
            bracket_generator(length, result, opened + 1, closed, line + '(')
        if opened > closed:
            bracket_generator(length, result, opened, closed + 1, line + ')')


def main():
    n = int(input())

    result = []
    bracket_generator(n, result=result)

    for line in result:
        print(line)


if __name__ == '__main__':
    main()
