"""
-- ПРИНЦИП РАБОТЫ --
1) Выполняем проверку общей суммы очков, если она нечетная => разбиение невозможно.

2) Нужно найти последовательность, которая в сумме даст sum / 2, где sum - общая сумма всех очков.

3) Если такая последовательность найдена => задача решена.

Задачу будем решать с помощью динамического программирования, постепенно увеличивая кол-во элементов
в последовательности, и проверять предыдущими комбинациями.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Мы последовательно перебираем все пары, используя предыдущее значение для уже рассчитанных пар.
Если решения нет, значит его невозможно получить, поскольку уже будут произведены все сравнения.
Иначе - решение найдено

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Так как мы обходим массив размерностью sum / 2, то временная сложность будет O(n * sum / 2),
где n - кол-во партий, sum - общая сумма очков.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для расчетов мы храним массив размерностью sum / 2, значит сложность O(sum / 2), где sum - общая сумма очков.
"""

"""
-- ID успешной посылки --
63668166
"""


def main():
    n = int(input().strip())

    scores = []

    all_sum = sum(scores)

    if n == 0:
        possibility = True
    elif all_sum % 2 != 0:
        possibility = False
    else:
        half_sum = all_sum // 2

        dp = [False] * (half_sum + 1)

        for i in range(n):
            for j in range(half_sum, scores[i] - 1, -1):
                if dp[j - scores[i]] or (scores[i] == j):
                    dp[j] = True

        possibility = dp[half_sum]

    print(str(possibility))


if __name__ == '__main__':
    main()
