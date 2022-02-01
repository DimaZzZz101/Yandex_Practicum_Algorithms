"""
-- ПРИНЦИП РАБОТЫ --
Сначала создаем trie (бор) на основе допустимых слов, а дальше смотрим по бору, куда можем попасть.

### Дополнил код некоторыми комментариями и привел пример назначения массива valid.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Идея решения была взята из теории к спринту, а именно часть про префиксное дерево.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Функция построения префиксного дерева работает за O(L), где L — суммарная длина слов во множестве.

Функция нахождения разбиений работает за O(N * M), где N — длина текста,
                                                       M = max(Mi) - длина самого длинного из искомых шаблонов.

### На предыдущей итерации отправки ошибся, временная сложность будет такой (не пространственная):
Итоговая временная сложность составляет: T * O(L) + O(N * M), где T - кол-во допустимых слов.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Память для хранения префиксного дерева составляет O(L), где L — суммарная длина слов во множестве,
                                                                такое возможно, если у всех слов разные префиксы,
                                                                т.е. худший случай.

Еще необходима память под массив терминальных элементов, равная O(K), где K - кол-во элементов в боре.

Память для хранения достижимых позиций равна O(n), где n - длина строки.
"""

"""
-- ID успешной посылки --
64526502
"""


# Добавление слова в бор.
def add_string(trie, terminals, string):
    current_node = trie[0]
    current_node_index = 0

    for char in string:
        if char not in current_node:
            current_node[char] = len(trie)
            trie.append({})
            terminals.append(False)

        next_node_index = current_node[char]
        current_node = trie[next_node_index]
        current_node_index = next_node_index

    terminals[current_node_index] = True


def break_words(trie, terminals, string):
    # valid - проверочный массив узлов, в котором терминальный (выходной) узел - True, а нетерминальный узел - false.
    # То есть если в trie есть такая последовательность узлов, что некоторая последовательность символов в слове равна
    # первой, то в массиве valid значение True будет расположено там, где заканчивается подслово в слове.
    # Приведу пример:
    #   Пусть входное слово: examiwillpasstheexam
    #   Тогда массив valid для него будет: [T, F, F, F, T, T, F, F, F, T, F, F, F, T, F, F, T, F, F, F, T]
    #   Собственно заполнение valid происходит при помощи бора, но для наглядности я сравню исходную строку и valid:
    #      [e, x, a, m, i, w, i, l, l, p, a, s, s, t, h, e, e, x, a, m]
    #       |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    #       v  v  v  V  V  v  v  v  V  v  v  v  V  v  v  V  v  v  v  V
    #   [T, F, F, F, T, T, F, F, F, T, F, F, F, T, F, F, T, F, F, F, T]
    #   Первый элемент массива valid = True, чтобы не нарушалась общая логика.

    valid = [True] + [False] * len(string)

    for pos in range(len(string)):
        if not valid[pos]:
            continue

        # Начинаем с корня бора.
        current_node = trie[0]

        # Перебираем символы шаблона, начиная со стартовой позиции.
        offset = 0

        while pos + offset < len(string):
            symbol = string[pos + offset]

            # Если подходящее ребро в дереве отсутствует.
            if symbol not in current_node:
                break

            # Сдвиг на следующий символ.
            next_index = current_node[symbol]
            current_node = trie[next_index]

            # Если текущий узел терминальный и в него можно попасть из предыдущей позиции,
            # то отмечаем позицию, как достижимую.
            if terminals[next_index]:
                valid[pos + offset + 1] = True
            offset += 1

    # Поскольку нужно добраться до конца строки - смотрим на последний элемент.
    return valid[len(string)]


if __name__ == "__main__":
    # Бор и выходные узлы.
    trie = [{}]

    # Массив узлов: True - терминальный узел (выходной), False - не терминальный
    terminals = [False]

    string = input()
    n = int(input())

    # Заполняем бор.
    for _ in range(n):
        dict_word = input()
        add_string(trie, terminals, dict_word)

    # Проверка возможности разбиения.
    is_valid = break_words(trie, terminals, string)

    print("YES" if is_valid else "NO")
