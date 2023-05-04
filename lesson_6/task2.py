import math


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return (perimeter, area, diagonal)


if __name__ == '__main__':
    side = int(input("Enter the side of the square: "))
    print(square(side))
