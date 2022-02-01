def is_prime(numbers):
    if ((numbers[0] % 2 == 0) and (numbers[1] % 2 == 0) and (numbers[2] % 2 == 0)) or (
            (numbers[0] % 2 != 0) and (numbers[1] % 2 != 0) and (numbers[2] % 2 != 0)):
        return "WIN"
    else:
        return "FAIL"


if __name__ == "__main__":
    numbers = [int(num) for num in input().split(' ')]

    print(is_prime(numbers))
