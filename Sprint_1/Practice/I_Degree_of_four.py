import math


def is_degree(num):
    if num == 1 or num == 4:
        print('True')
    elif math.sqrt(num) != 4:
        print('False')
    else:
        print('True')


if __name__ == "__main__":
    num_in_degree = int(input())

    print(is_degree(num_in_degree))
