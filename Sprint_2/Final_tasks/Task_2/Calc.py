"""
-- ПРИНЦИП РАБОТЫ --
Для вычисления значения выражения, записанного в обратной польской нотации, нужно считывать выражение слева направо,
выполняя следующие шаги:
    1) Обработка входного символа:
        1.1) Если на вход подан операнд, он помещается на вершину стека.
        1.2) Если на вход подана операция, то она выполняется над требуемым количеством значений из стека, взятых в
          порядке добавления.
        1.3) Результат выполненной операции помещается на вершину стека.
        1.4) Если входной набор символов обработан не полностью, перейти к шагу 1.1.
    2) После полной обработки входного набора символов результат вычисления находится в вершине стека.
    3) Если же в стеке осталось несколько чисел, то надо вывести только верхний элемент.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Для доказательства можно обратиться к описанию работы польской нотации:
    - Когда в выражении встречается знак операции, то она выполняется над двумя ближайшими операндами, находящимися слева
    от знака операции.
    - Результат операции заменяет в выражении последовательность её операндов и знак, после чего выражение вычисляется
    дальше по тому же правилу.
    - Числа добавляем в стэк - это и будут ближайшие операнды. Как только встречаем операцию - достаем их (операнды).
    - Добавляем результат в стэк. Получается, что заменяется операция над двумя операндами на их результат, что и
    требовалось по заданию.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции вставки и удаления последнего элемента массива происходит за O(1).
Т.к. мы перебираем все символы входного выражения, то сложность будет итоговая сложность будет O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
На каждую операцию приходится 2 числа, следовательно в стэке будет n/2 элементов (в среднем).
В худшем случае будет n - 1 элемент. Поэтому в итоге пространственная сложность будет O(n).
"""

"""
-- ID успешной посылки --
54889873
"""

"""
Возможно, я не совсем правильно понял Вашу идею со словарем, но
при его добавлении столкунлся с проблемой его использования сразу же
пришла мысль сделать его частью класса. 
Ниже новая реализация:
    - некоторые функции были внесены в класс, теперь класс - цельная сущность
        для калькулятора;
    - выражение приводится к виду: числа и знаки, далее присходит вычисление;
    - вместо отдельных констант был добавлен словарь с ключами - знаки операторов,
      и значениями - методы класса StackCalculator, соответсвующие той или иной операции.
"""


class StackCalculator:
    def __init__(self, array=None):
        self.stack = [] if array is None else array

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def adding(self, first_operand, second_operand):
        result = first_operand + second_operand
        self.stack.append(result)
        return self.stack

    def multiplication(self, first_operand, second_operand):
        result = first_operand * second_operand
        self.stack.append(result)
        return self.stack

    def subtract(self, first_operand, second_operand):
        result = first_operand - second_operand
        self.stack.append(result)
        return self.stack

    def division(self, first_operand, second_operand):
        result = first_operand // second_operand
        self.stack.append(result)
        return self.stack

    # Метод, возвращающий последний элемент стека - результат работы калькулятора.
    def peak(self):
        if self.is_empty():
            print('The stack is empty')
        print(self.stack[-1])

    def stack_calculator(self, data):
        operators = {'+': self.adding,
                     '-': self.subtract,
                     '*': self.multiplication,
                     '/': self.division,
                     }
        for element in data:
            if not operators.get(element):
                self.push(element)
            else:
                second_operand = self.stack.pop()
                first_operand = self.stack.pop()
                operators[element](first_operand, second_operand)
        return self.peak()


def to_digit(data):
    for i in range(len(data)):
        try:
            data[i] = int(float(data[i]))
        except ValueError:
            pass
    return data


def main():
    try:
        expression = to_digit(list(map(str, input().split())))
    except EOFError:
        expression = []

    stack = StackCalculator()
    stack.stack_calculator(expression)


if __name__ == '__main__':
    main()
