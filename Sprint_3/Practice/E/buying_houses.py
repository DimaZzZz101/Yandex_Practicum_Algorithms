def buying_houses():
    homes_num, money = map(int, input().strip().split())
    homes = list(map(int, input().strip().split()))[:homes_num]
    bought = 0

    for home in sorted(homes):
        if home > money:
            break
        money -= home
        bought += 1

    return bought


if __name__ == '__main__':
    print(buying_houses())
