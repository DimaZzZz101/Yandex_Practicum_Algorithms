def factorisation(n):
    answer = []
    divider = 2
    while divider * divider <= n:
        if n % divider == 0:
            answer.append(divider)
            n //= divider
        else:
            divider += 1
    if n > 1:
        answer.append(n)

    return answer


n = int(input())

print(*factorisation(n))
