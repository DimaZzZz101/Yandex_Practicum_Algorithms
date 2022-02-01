if __name__ == "__main__":
    original_string = input().strip()

    n = int(input().strip())

    inserts = [(0, '')] * n

    for i in range(n):
        sub, pos = input().strip().split()
        inserts[i] = (int(pos), sub)

    new_string = ''

    offset = 0

    for pos, sub in sorted(inserts):
        new_string += original_string[offset:pos] + sub
        offset = pos

    new_string += original_string[offset:]

    print(new_string)
