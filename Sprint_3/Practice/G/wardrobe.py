COLOR_PINK = '0'
COLOR_YELLOW = '1'
COLOR_CRIMSON = '2'


def sort_colours():
    colours_count = int(input())
    colors = input().strip().split()[:colours_count]

    pink = []
    yellow = []
    crimson = []

    for color in colors:
        if color == COLOR_PINK:
            pink.append(color)
            continue

        if color == COLOR_YELLOW:
            yellow.append(color)
            continue

        if color == COLOR_CRIMSON:
            crimson.append(color)
            continue

    return ' '.join(pink + yellow + crimson)


if __name__ == '__main__':
    print(sort_colours())
