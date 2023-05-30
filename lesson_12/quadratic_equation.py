###
import math


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, None
    else:
        return None, None
