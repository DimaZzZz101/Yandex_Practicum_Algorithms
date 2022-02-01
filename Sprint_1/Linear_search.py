def find_element(numbers, x):
    for i in range(len(numbers)):  # Проходим по всем элементам массива.
        if numbers[i] == x:  # Сравниваем их с иксом.
            return i  # Если нашли - возвращаем индекс.
    return -1  # Если не нашли - возвращаем -1.


if __name__ == "__main__":
    print(find_element([1, 2, 3, 4, 5, 6], 4))
    print(find_element([1, 2, 3, 4, 5, 6], 7))
