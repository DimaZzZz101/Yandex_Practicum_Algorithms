import sys

"""
-- ПРИНЦИП РАБОТЫ --
Принцип работы алгоритма описан в условии задачи.
Вместо выделения O(n) дополнительной памяти мы создаем указатели на элементы, которые будем двигать.
Сверяемся поэлементно с опорным элементом и меняем элементы местами, если требуется.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Мы не копируем массив => не выделяем память => мы получаем выигрыш в памяти как и требуется в задании.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Данный алгоритм является модификацией QuickSort. 
    - В худщем случае сложность будет: O(n^2)
    - В общем случае сложность будет:  O(n * log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Поскольку мы храним только указатели и ссылку на массив,
то без учета входных данных сложность будет: O(n).
    - Земечание:
        Сам алгоритм использует константную память, т.е. О(1).
        
        После разделения исходного массива на две части, для работы с первой из них тратится O(log(n)) памяти, так как
        каждый раз будет выделяться помять при рекурсии и мы сокращаем эту часть. Что касается второй части, то она
        будет обрабатываться автоматичести при "подъме" в стеке вызовов =>  под работу со вторым разделением мы уже не
        тратим пямять. Значит в среднем случае будет O(log(n)) пространственной сложности.
        
        В худшем случае O(n).
"""

"""
-- ID успешной посылки --
55956711
"""

"""
# Попытался применить совет по вынесению разделения массива в отдельную функцию,
# видимо при больших входных данных программа не справлялется с выделением памяти
# под рекурсивные вызовы:

Лог теста 20:
-----------------------------------------------------------------------------------
Traceback (most recent call last):
  File "f6e29e7a-d9e9-498d-b080-27eb35f79dba", line 80, in <module>
    quick_sort(participants, 0, n - 1)
  File "f6e29e7a-d9e9-498d-b080-27eb35f79dba", line 67, in quick_sort
    quick_sort(array, start_, right)
  File "f6e29e7a-d9e9-498d-b080-27eb35f79dba", line 67, in quick_sort
    quick_sort(array, start_, right)
  File "f6e29e7a-d9e9-498d-b080-27eb35f79dba", line 67, in quick_sort
    quick_sort(array, start_, right)
  [Previous line repeated 993 more times]
  File "f6e29e7a-d9e9-498d-b080-27eb35f79dba", line 65, in quick_sort
    right, left = partition(array, start_, end_)
  File "f6e29e7a-d9e9-498d-b080-27eb35f79dba", line 45, in partition
    while array[left] < pivot:
RecursionError: maximum recursion depth exceeded in comparison
-----------------------------------------------------------------------------------

def partition(array, start_, end_):
    # Задаем опорную точку и указатели на начало и конец.
    pivot = array[(start_ + end_) // 2]
    left = start_
    right = end_

    while left <= right:
        # Пока возможно двигаем левый указатель к правому.
        while array[left] < pivot:
            left += 1
        # Пока возможно сдвигаем правый указатель к левому.
        while array[right] > pivot:
            right -= 1

        # Меняем указатели местами.
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

        return right, left


def quick_sort(array, start_, end_):
    right, left = partition(array, start_, end_)

    quick_sort(array, start_, right)
    quick_sort(array, left, end_)
"""


def quick_sort(array, start_, end_):
    # Базовый случай.
    if start_ >= end_:
        return

    # Задаем опорную точку и указатели на начало и конец.
    pivot = array[(start_ + end_) // 2]
    left = start_
    right = end_

    while left <= right:
        # Пока возможно двигаем левый указатель к правому.
        while array[left] < pivot:
            left += 1
        # Пока возможно сдвигаем правый указатель к левому.
        while array[right] > pivot:
            right -= 1

        # Меняем указатели местами.
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quick_sort(array, start_, right)
    quick_sort(array, left, end_)


if __name__ == '__main__':
    n = int(input())
    participants = []

    # Считываеие парметров участников: логин, количество решенных задач, величина штрафа.
    for _ in range(n):
        login, tasks_count, penalty = sys.stdin.readline().strip().split()
        participants.append((-int(tasks_count), int(penalty), login))

    quick_sort(participants, 0, n - 1)

    # Вывод отсортированного массива.
    for person in participants:
        print(person[2])
