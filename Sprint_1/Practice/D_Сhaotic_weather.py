def find_chaotic(temperatures, n):
    chaotic = []

    if n > 1:
        if temperatures[0] > temperatures[1]:
            chaotic.append(temperatures[0])
        for i in range(1, n - 1):
            if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
                chaotic.append(temperatures[i])
        if temperatures[n - 1] > temperatures[n - 2]:
            chaotic.append(temperatures[n - 1])
    else:
        chaotic.append(temperatures[0])

    return chaotic


if __name__ == "__main__":
    n = int(input())
    temperatures = [int(t) for t in input().split(' ')]

    print(len(find_chaotic(temperatures, n)))
