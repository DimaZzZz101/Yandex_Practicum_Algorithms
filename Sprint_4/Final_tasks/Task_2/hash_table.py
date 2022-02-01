import sys

"""
-- ПРИНЦИП РАБОТЫ --
# Принцип работы был хорошо описан в теории к спринту 4.
Я реализовал структуру данных Hash-table, в которой задется MAX_SIZE возможное кол-во "корзин" (buckets), 
как требовалось в условии 99991 < 10^5.

Также по условию, для вычисления корзины, я использую остаток от деления на MAX_SIZE (исходя из того,
что все ключи целые). Далее, вычислив корзину, сохраняем в нее пары (key, value). 

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Фактически, я реализовывал хеш-таблицу по теории к спринту. Как было сказано ранее там все подробно описано.
Честно говоря, не знаю, что еще можно добавить.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
У нас определены граничные условия (размер и диапазон ключей n):
    - Временная сложность O(Const) , где Const в худшем случае n / size = 10^4.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В худшем случае мы будем иметь сложность O(n), где n - кол-во ключей.
"""

"""
-- ID успешной посылки --
56740580
"""

# Простое число < 10^5
MAX_SIZE = 99991

# Команды:
GET = 'get'
PUT = 'put'
DELETE = 'delete'


# Класс хеш-таблица.
class HashTable:
    def __init__(self, max_size=MAX_SIZE):
        self.max_size = max_size
        self.buckets = tuple(([] for _ in range(max_size)))

    # Метод получения ключа в таблице.
    def _get_bucket_(self, key):
        return key % self.max_size

    # Получение значения по ключу.
    def get(self, key):
        bucket = self.buckets[self._get_bucket_(key)]
        if len(bucket) == 0:
            return None
        for value in bucket:
            if value[0] == key:
                return value[1]
        return None

    # Метод добавления пары ключ-значение.
    def put(self, key, value):
        bucket = self.buckets[self._get_bucket_(key)]
        if len(bucket) == 0:
            bucket.append((key, value))
            return
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                if bucket[i][1] != value:
                    bucket[i] = (key, value)
                return
        bucket.append((key, value))
        return

    # Метод удаления ключа из таблицы.
    def delete(self, key):
        bucket = self.buckets[self._get_bucket_(key)]
        length = len(bucket)
        if length == 0:
            return None
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                if length == 1 or i == (length - 1):
                    return bucket.pop()[1]
                bucket[i], bucket[-1] = bucket[-1], bucket[i]
                return bucket.pop()[1]
        return None


def main():
    n = int(input())
    hash_table = HashTable()

    for _ in range(n):
        args = sys.stdin.readline().strip().split()

        if args[0] == GET:
            print(hash_table.get(int(args[1])))
        elif args[0] == PUT:
            hash_table.put(int(args[1]), int(args[2]))
        elif args[0] == DELETE:
            print(hash_table.delete(int(args[1])))
        else:
            raise RuntimeError(f'Ошибка: Неизвестная команда: {args[0]}')


if __name__ == '__main__':
    main()
