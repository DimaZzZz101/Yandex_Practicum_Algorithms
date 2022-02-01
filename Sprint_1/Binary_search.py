def find_element(numbers, x):
    low = 0  # Левая граница.
    high = len(numbers) - 1  # Правая граница.

    while low <= high:
        mid = (low + high) // 2  # Находим середину.
        guess = numbers[mid]

        if guess == x:
            return mid  # Если нашли число.
        if guess > x:
            high = mid - 1  # Если число меньше найденного.
        else:
            low = mid + 1  # Если число больше найденного.
    else:
        return -1  # Если не нашли число.


if __name__ == "__main__":
    print(find_element([1, 2, 3, 4, 5, 6], 4))
    print(find_element([1, 2, 3, 4, 5, 6], 7))
