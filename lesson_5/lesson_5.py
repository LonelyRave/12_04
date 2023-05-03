# Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c),
# якщо дискримінант від'ємний викликати виняток DiscriminantError і вивести відповідне повідомлення.


import math


class DiscriminantError(Exception):
    pass


a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

try:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        raise DiscriminantError("Discriminant is negative, cannot take square root of negative number.")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("The equation has one real root: x =", x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("The equation has two real roots: x1 =", x1, "and x2 =", x2)
except DiscriminantError as e:
    print("Error:", e)


# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа,
# оператора (як мінімум + і -) та іншого числа, розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()
#
# a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
#
# b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)).
#    Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
#
# c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError


class FormulaError(Exception):
    pass


while True:
    try:
        expression = input("Enter expression: ")
        elements = expression.split()

        if len(elements) != 3:
            raise FormulaError("Invalid expression: should consist of 3 elements separated by space")

        try:
            num1 = float(elements[0])
        except ValueError:
            raise FormulaError("Invalid first element: must be a number")

        try:
            num2 = float(elements[2])
        except ValueError:
            raise FormulaError("Invalid third element: must be a number")

        operator = elements[1]
        if operator not in ["+", "-"]:
            raise FormulaError("Invalid operator: must be + or -")

        if operator == "+":
            result = num1 + num2
        else:
            result = num1 - num2

        print("Result:", result)

    except FormulaError as e:
        print(e)

    except KeyboardInterrupt:
        print("Exiting...")
        break

