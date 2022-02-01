import sys
from collections import Counter
from heapq import nsmallest

"""
-- ПРИНЦИП РАБОТЫ --
Сперва мы создаем индекс - хеш-таблица с элементами (id документа, кол-во вхождений),
далее считаем релевантность по каждому запросу и сортируем результат.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# При считывании строк я использую Counter - вид словаря,
# который будет подсчитывать вхождения элементов в документе/запросе.

Изначально считываем документы и заполняем словарь такого вида:
    { слово: { номер_документа: кол-во слов в документе  } }
После этого считываем запросы и сразу находим релевантности, вызывая функцию поиска.

Из запроса делаем set, чтобы итерироваться только по уникальным словам

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность состоит из двух компонент:
    1) Поисковый индес заполняется за O(n), операции со словарем выполняются за О(1));
    2) Поиск релевантных документов по одному запросу:
        - Вызываем функцию нахождения релевантности m раз (поэтому О(m),
          операции со словарем также выполняются за O(1));
        - Сортировка массива происходит за O(k*log(k)), где k - кол-во совпавших слов;

В итоге результирующая сложность: O(n + m * k * log(k))

Временная сложность O(n * m * k*log(k)) - где
    n - кол-во уникальных слов в индексе (индекс заполняется за O(n), операции со словарем выполняются за О(1));
    m - кол-во вызовов функции нахождения релевантности (поэтому О(m), операции со словарем также выполняются за O(1));
    k - кол-во совпавших слов (поэтому сортировка массива происходит за O(k*log(k));
    
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность O(n) - общем случае
    - для хранения индекса: O(n) - в худшем случае, где n - суммарное кол-во уникальных слов в документах;
    - для хранения запросов: O(k) на каждой итерации, где k - кол-во повторений каждого слова в докуменах;
"""

"""
-- ID успешной посылки --
57027442
"""

LIMIT = 5


def create_index(n):
    index = {}

    for idx in range(n):
        document = Counter(sys.stdin.readline().strip().split())

        for word in document:
            word_index = index.get(word)
            index_el = (idx + 1, document[word])

            if word_index is None:
                index[word] = [index_el]
            else:
                index[word].append(index_el)

    return index


def search_engine(query, index):
    relevant_results = {}

    for word in set(query):
        index_item = index.get(word)

        if index_item is None:
            continue

        for document_idx, count in index_item:
            relevance = relevant_results.get(document_idx)

            if relevance is None:
                relevant_results[document_idx] = count
            else:
                relevant_results[document_idx] += count

    return [result[0] for result in nsmallest(LIMIT, relevant_results.items(), key=lambda item: (-item[1], item[0]))]


def main():
    n = int(input())

    index = create_index(n)

    m = int(input())

    for _ in range(m):
        request = sys.stdin.readline().strip().split()
        docs = search_engine(request, index)

        if len(docs) > 0:
            print(' '.join(map(str, docs)))


if __name__ == '__main__':
    main()
