from collections import deque

DIGITS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def combinations_generator(sequence, result, line=''):
    if len(sequence) == 0:
        result.append(line)
        return line
    else:
        digit = int(sequence.popleft())
        for char in DIGITS.get(digit):
            combinations_generator(sequence.copy(), result, line + char)


def main():
    digit_sequence = input().strip()
    result = []
    combinations_generator(deque(digit_sequence), result=result)

    print(' '.join(result))


if __name__ == '__main__':
    main()
