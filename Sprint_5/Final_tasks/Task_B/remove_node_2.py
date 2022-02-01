"""
-- ПРИНЦИП РАБОТЫ --
По заданию необходимо найти узел с заданным значением.
Поскольку значения в дереве уникальны (по условию) - то алгоритм будет работать корректно при первом проходе дерева.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение соответствует алгоритму.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Примечание: сложность дана по условию.
Так как дерево является деревом поиска, то мы проходим по нему за O(H), где H высота дерева.
Поиск наибольшего элемента в поддереве также будет равен его высоте.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Поскольку мы работаем только со ссылками на узлы дерева, то выделяется О(1) пямяти для харнения этих ссылок на узлы,
которые необходимо удалить, а также на родителя удаляемого узла. Но так как происходят рекурсивные вызовы во время
прохода по дереву, то для хранения вызовов в стеке потребуется О(H) памяти, где H - высота дерева.
"""

"""
-- ID успешной посылки --
60626124
"""

# # Структура узла.
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.value = value
#         self.right = right
#         self.left = left


def min_value(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def remove(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        tmp = min_value(root.right)

        root.value = tmp.value

        root.right = remove(root.right, tmp.value)

    return root
