class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def calculate_area(self):
        area = abs((self.point1.x * (self.point2.y - self.point3.y) + self.point2.x * (self.point3.y - self.point1.y) +
                    self.point3.x * (self.point1.y - self.point2.y)) / 2)
        return area if area > 0 else None


class Square:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def calculate_area(self):
        side1 = ((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2) ** 0.5
        side2 = ((self.point2.x - self.point3.x) ** 2 + (self.point2.y - self.point3.y) ** 2) ** 0.5
        side3 = ((self.point3.x - self.point4.x) ** 2 + (self.point3.y - self.point4.y) ** 2) ** 0.5
        side4 = ((self.point4.x - self.point1.x) ** 2 + (self.point4.y - self.point1.y) ** 2) ** 0.5

        if side1 == side2 == side3 == side4:
            return side1 ** 2
        else:
            return None
