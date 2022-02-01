import sys


def find_day(money, cost, start=0):
    left = start - 1 if start > 0 else 0
    right = len(money) - 1

    while left <= right:
        mid = (left + right) // 2

        if money[mid] >= cost:
            if mid == 0 or money[mid - 1] < cost:
                return mid + 1

            right = mid

            continue

        if money[mid] < cost:
            if mid < len(money) - 2:
                left = mid
            else:
                left = mid + 1

    return -1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    money = list(map(int, sys.stdin.readline().split()))
    cost = int(sys.stdin.readline())

    day1 = find_day(money, cost)
    day2 = find_day(money, 2 * cost, day1)

    print(day1, day2)
