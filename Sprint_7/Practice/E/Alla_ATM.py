import sys


def main():
    amount = int(input().strip())
    n = int(input().strip())

    min_banknotes = [0] + [sys.maxsize] * amount
    banknotes = set(sorted(list(map(int, input().strip().split()))[:n]))

    # F_0 = 0
    # F_1 = F_a_1 = F_a_n = 1
    # F_n = min((F_n - F_a_1), (F_n - F_a_2), (F_n - F_a_3)) + 1
    for note in banknotes:
        if note > amount:
            continue

        min_banknotes[note] = 1

    if min_banknotes[amount] == sys.maxsize:
        for summa in range(1, amount + 1):
            for note in banknotes:
                if summa >= note and min_banknotes[summa] > min_banknotes[summa - note] + 1:
                    min_banknotes[summa] = min_banknotes[summa - note] + 1

    if min_banknotes[amount] < sys.maxsize:
        print(str(min_banknotes[amount]))
    else:
        print('-1')


if __name__ == '__main__':
    main()
