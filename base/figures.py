import math


class Figure:
    def __init__(self, name, area, angles, perimeter):
        self.name = name
        self.area = area
        self.angles = angles
        self.perimeter = perimeter


class Triangle(Figure):
    _angles = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def tr_name():
        return 'Треугольник'

    def tr_perimeter(self):
        return self.a + self.b + self.c

    def tr_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt((p * (p - self.a) * (p - self.b) * (p - self.c)))



class Rectangle(Figure):
    _angles = 4

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def rect_name():
        return 'Прямоугольник'

    def rect_perimeter(self):
        return (self.width + self.height) * 2

    def rect_area(self):
        return (self.width * self.height)


class Square(Figure):
    _angles = 4

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def sq_name(self):
        return ('Квадрат')

    def sq_perimeter(self):
        return (self.width + self.height) * 2

    def sq_area(self):
        return (self.width * self.height)


class Circle(Figure):
    _angles = 0

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def c_name():
        return ('Круг')

    def c_perimeter(self):
        return (math.pi * self.radius * 2)

    def c_area(self):
        return (math.pi * self.radius ** 2)


def add_square(figure1, figure2):
    figure1 = figure1.tr_area()
    figure2 = figure2.rect_area()
    total_area = int(figure1 + figure2)
    return f'Площадь фигур = {total_area}'

print (add_square(Triangle(2, 3, 4), Rectangle(3, 4)))