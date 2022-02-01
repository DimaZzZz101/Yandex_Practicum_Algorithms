def bin_sum_numbers(bin_num1, bin_num2):
    result = []

    d = len(bin_num1) - len(bin_num2)

    if d > 0:
        for m in range(d):
            bin_num2.append(0)
    elif d < 0:
        for n in range(-d):
            bin_num1.append(0)

    for j in range(max(len(bin_num1), len(bin_num2)) + 1):
        result.append(0)

    for i in range(len(bin_num1)):
        result[i] = (int(result[i])) + (int(bin_num1[i])) + (int(bin_num2[i]))
        if result[i] == 2:
            result[i] = 0
            result[i + 1] = 1
        elif result[i] == 3:
            result[i] = 1
            result[i + 1] = 1
    if result[::-1][0] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))


if __name__ == "__main__":
    a = list(map(int, str(input())))[::-1]
    b = list(map(int, str(input())))[::-1]

    print(bin_sum_numbers(a, b))
