from task_2 import Point, Triangle, Square
from task_3 import PhoneBook, Contact, Interface


def main():
    
    point1 = Point(0, 0)
    point2 = Point(0, 4)
    point3 = Point(3, 0)

    triangle = Triangle(point1, point2, point3)
    triangle_area = triangle.calculate_area()

    if triangle_area is not None:
        print(f"The area of the triangle is: {triangle_area}")
    else:
        print("Invalid triangle coordinates. Cannot calculate area.")

    point4 = Point(4, 0)

    square = Square(point1, point2, point3, point4)
    square_area = square.calculate_area()

    if square_area is not None:
        print(f"The area of the square is: {square_area}")
    else:
        print("Invalid square coordinates. Cannot calculate area.")

    
    phone_book = PhoneBook()
    interface = Interface(phone_book)
    interface.start()

    print("Program completed successfully.")


if __name__ == '__main__':
    main()
