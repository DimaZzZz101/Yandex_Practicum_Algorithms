from string import digits

"""
-- ПРИНЦИП РАБОТЫ --
Чтобы решить данную задачу, можно разбить ее на две подзадачи:
    1. Распаковка строки: посимвольно считываем строку. Если строка требует распаковки,
       то делаем это рекурсивно, считая правильную последовательность скобок.
       Чтобы оптимизировать распаковку было добавлено кеширование.

    2. Поиск общего префикса: посимвольно сравниваем каждый символ
       строки с другим символом на этой позиции. Когда нашли длину - выводим сам префикс.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
На мой взгляд алгоритм корректен, так как большая часть рассуждений была взята из теории к спринту, а именно:
    - расчет префикс-функции;
    - эффективный поиск шаблона в тексте.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Запишу временную сложность сначала для подзадач:
    - Для распаковки строки:
        O (M * N * K) - где M - длина строки (максимальная),
                            K - кол-во вложенных уровней выражения,
                            N - кол-во строк.

    - Для поиска общего префикса:
        O (M * N) - где M - длина строки (максимальная),
                        N - кол-во строк.

В итоге имеем следующую общую сложность алгоритма: O(M*N) + O(M*N*K) = O(M*N + M*N*K)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственную сложность также распишу для подзадач:
    - Для распаковки строк O(M*N) (с учетом кеширования), где M - длина строки (максимальная),
                                                              N - кол-во строк.
    - Для поиска префикса - сложность O(1).
"""

"""
-- ID успешной посылки --
64520635	
"""

"""
Чтобы упростить программу, я решил провести небольшой рефакторинг: выделил в отдельную функцию поиск скобок и упростил 
саму распаковку. Также упростил функцию поиска префикса. После изменений в коде могу выделить следующее:
    - мое предыдущее деление на подзадачи остается корректным (вынося функцию поиска скобок из распаковки, я не нарушаю
      асимптотику;
    - поиск префикса также глобально не изменился;
    - сложность по памяти и по времени осталась такой же.
"""

OPEN_BRACKET = '['
CLOSE_BRACKET = ']'


def find_bracket(string):
    dif_brackets = 0
    for i in range(len(string)):
        if string[i] == OPEN_BRACKET:
            dif_brackets += 1
        elif string[i] == CLOSE_BRACKET:
            dif_brackets -= 1

        if dif_brackets == 0:
            return i


def unpack(string):
    unpack_string = ""

    i = 0

    while i != len(string):
        char = string[i]

        if char in digits:
            num_repeats = int(char)
            index = find_bracket(string[i + 1:])
            suffix = unpack(string[i + 2:i + 1 + index])
            unpack_string += suffix * num_repeats
            i += index + 2
        elif char:
            unpack_string += char
            i += 1

    return unpack_string


def find_prefix(strings):
    prefix = None

    for string in strings:
        unpack_string = unpack(string)

        if prefix is None:
            prefix = unpack_string
        else:
            for i in range(min(len(unpack_string), len(prefix))):
                if prefix[i] != unpack_string[i]:
                    prefix = prefix[:i]
                    break

        if prefix == "":
            return prefix

    return prefix


if __name__ == '__main__':
    n = int(input().strip())
    strings = list()

    for i in range(n):
        strings.append(input())

    print(find_prefix(strings))
