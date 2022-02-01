import math as m

if __name__ == '__main__':
    nodes = int(input())

    print(int(m.factorial(2 * nodes) / (m.factorial(nodes) * m.factorial(nodes + 1))))
