brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


class Stack:
    def __init__(self, array=None):
        self.stack = [] if array is None else array

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)
        return self.stack


def is_correct_bracket_seq(sequence):
    stack = Stack()

    for char in sequence:
        if char in '{([<':
            stack.push(char)
            continue

        if char in '})]>':
            try:
                if stack.pop() != brackets.get(char):
                    return False
            except IndexError:
                return False

    if not stack.is_empty():
        return False

    return True


def main():
    sequence = list(input().strip())
    print(is_correct_bracket_seq(sequence))


if __name__ == '__main__':
    main()
