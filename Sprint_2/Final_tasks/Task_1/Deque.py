import sys

"""
-- ПРИНЦИП РАБОТЫ --
Дек я реализовал на кольцевом буфере, который был предложен в теории к спринту для очереди, но доработал его.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Мы всегда идем по массиву и считаем счетчик для контроля переполненеия.
- Добавляем элемент:
    Если в начало, то элемент будет на первой позиции в массиве;
    Если в конец, то элемент будет на нулевой позиции в массиве;
        Пример:
            1) Добавляю элемент в начало очереди, т.е. он становится на 1ую позицию, значит позиция следующего
            добавленного в начало элемента будет 2.
            2) Добавляю элемент в конец очереди, т.е. он становится на 0ую позицию. Тогда по логике примера 1 следующий
            элемент, добавленный в конец, будет находиться на позиции 0 - 1 = -1, что неверно. Поэтому все индексы
            берутся по модулю max_n. В таком случае индекс будет равен max_n - 1.

- Извлекаем элемент:
    Логика: берем значение по индексу до головы (head) и после хвоста (tail), тоже по модулю max_n.

- Реализована проверка на переполнение и постоту, при добавлении и удалении соответственно.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Поскольку размер массива заранее известен, то реалокации в памяти не будет - это обеспечивает добавление элемента
за O(1). Также мы всегда работаем с массивом по индексу => все методы класса Deque будут просто обращаться к той или
иной ячейке массива, а такое обращение занимает O(1), значит и все операции будут занимать O(1).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дек, содержащий n элементов, занимает O(n) памяти. Так же помять используется для хранения значения счетчиков.
В итоге сложность имеем пространственную сложность O(n).
"""

"""
-- ID успешной посылки --
54891196
"""

# Commands
PUSH_BACK = 'push_back'
PUSH_FRONT = 'push_front'
POP_FRONT = 'pop_front'
POP_BACK = 'pop_back'


class Deque:
    def __init__(self, n):
        self.deque = [None] * n
        self.max_n = n
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_back(self, element):
        if self.size == self.max_n:
            raise OverflowError('Deque is full.')

        self.tail = (self.tail - 1) % self.max_n
        self.size += 1

        self.head = (self.tail + self.size - 1) % self.max_n
        self.deque[self.tail] = element

    def push_front(self, element):
        if self.size == self.max_n:
            raise OverflowError('Deque is full')

        self.head = (self.head + 1) % self.max_n
        self.size += 1

        self.tail = (self.head - self.size + 1) % self.max_n
        self.deque[self.head] = element

    def pop_back(self):
        if self.size == 0:
            raise ValueError('Deque is empty')

        item = self.deque[self.tail]

        self.tail = (self.tail + 1) % self.max_n
        self.size -= 1

        self.head = (self.tail + self.size - 1) % self.max_n

        return item

    def pop_front(self):
        if self.size == 0:
            raise ValueError('Deque is empty')

        element = self.deque[self.head]

        self.head = (self.head - 1) % self.max_n
        self.size -= 1

        self.tail = (self.head - self.size + 1) % self.max_n
        return element


def process_command():
    commands_number = int(sys.stdin.readline().strip())
    max_size_ = int(sys.stdin.readline().strip())

    deque = Deque(max_size_)
    for _ in range(commands_number):
        cmd = input().strip().split()

        if cmd[0] == PUSH_FRONT:
            try:
                deque.push_front(int(cmd[1]))
            except OverflowError:
                print('error')
            continue

        if cmd[0] == POP_FRONT:
            try:
                print(deque.pop_front())
            except ValueError:
                print('error')
            continue

        if cmd[0] == PUSH_BACK:
            try:
                deque.push_back(int(cmd[1]))
            except OverflowError:
                print('error')

        if cmd[0] == POP_BACK:
            try:
                print(deque.pop_back())
            except ValueError:
                print('error')
            continue


if __name__ == '__main__':
    process_command()
