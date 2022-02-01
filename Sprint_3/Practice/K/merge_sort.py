def merge(arr, left, mid, right):
    first = arr[left:mid]
    second = arr[mid:right]

    if len(second) == 0:
        return first

    if len(first) == 0:
        return second

    result = [0] * (len(first) + len(second))

    l = 0
    r = 0
    k = 0

    while l < len(first) and r < len(second):
        # Выбираем, из какого массива забрать минимальный элемент.
        if first[l] <= second[r]:
            result[k] = first[l]
            l += 1
        else:
            result[k] = second[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в итоговый.
    while l < len(first):
        result[k] = first[l]  # left --> result
        l += 1
        k += 1

    while r < len(second):
        result[k] = second[r]  # right --> result
        r += 1
        k += 1

    return result


def merge_sort(arr, left, right):
    if (right - left) <= 1:
        return

    mid = (right + left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)

    merged_array = merge(arr, left, mid, right)

    m = 0

    for i in range(left, right):
        arr[i] = merged_array[m]
        m += 1


def main():
    sequence = list(map(int, input().strip().split()))
    merge_sort(sequence, 0, len(sequence))

    print(' '.join([str(element) for element in sequence]))


if __name__ == '__main__':
    main()
