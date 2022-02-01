cache = {}


def how_many(amount, banknotes: list):
    prob = tuple([amount] + banknotes)

    if prob in cache:
        return cache[prob]

    if amount == 0:
        return 1

    if len(banknotes) == 1:
        if amount % banknotes[0] == 0:
            return 1
        else:
            return 0

    total = 0
    n = 0

    while n * banknotes[0] <= amount:
        total += how_many(amount - n * banknotes[0], banknotes[1:])
        n += 1

    cache[prob] = total

    return total


if __name__ == '__main__':
    amount = int(input().strip())
    n = int(input().strip())

    banknotes = set(sorted(list(map(int, input().strip().split()))[:n]))

    print(how_many(amount, list(banknotes)))
