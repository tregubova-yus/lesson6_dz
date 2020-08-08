import pytest
import math

from base.figures import Triangle
from base.figures import Rectangle
from base.figures import Square
from base.figures import Circle


class Tests:

# Треугольник
    @pytest.mark.parametrize("vars_", argvalues=[(2, 3, 4)])
    def test_1_1(self, vars_):
        a = vars_[0]
        b = vars_[1]
        c = vars_[2]
        num = Triangle(a, b, c)
        p = (a + b + c) / 2
        x = math.sqrt((p * (p - a) * (p - b) * (p - c)))
        assert num.tr_area() == x

    @pytest.mark.parametrize("vars_", argvalues=[(2, 4, 4)])
    def test_1_2(self, vars_):
        a = vars_[0]
        b = vars_[1]
        c = vars_[2]
        num = Triangle(a, b, c)
        x = math.sqrt((a ** 2) + (b ** 2))
        assert c == int(x)

    @pytest.mark.parametrize("vars_", argvalues=[(11, 13, 17), (275, 164, 156)])
    def test_1_3(self, vars_):
        a = vars_[0]
        b = vars_[1]
        c = vars_[2]
        num = Triangle(a, b, c)
        x = a + b + c
        assert num.tr_perimeter() == x

    @pytest.mark.parametrize("vars_", argvalues=[(275, 164, 156)])
    def test_1_4(self, vars_):
        a = vars_[0]
        b = vars_[1]
        c = vars_[2]
        num = Triangle(a, b, c)
        x = a + b + c
        assert num.tr_perimeter() != 0

    @pytest.mark.parametrize("vars_", argvalues=[(2, 3, 4)])
    def test_1_5(self, vars_):
        a = vars_[0]
        b = vars_[1]
        c = vars_[2]
        num = Triangle(a, b, c)
        p = (a + b + c) / 2
        x = math.sqrt((p * (p - a) * (p - b) * (p - c)))
        y = math.sqrt((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)) / 4
        assert num.tr_area() == x
        assert y == x

# Прямоугольник
    @pytest.mark.parametrize("vars_", argvalues=[(20, 40)])
    def test_2_1(self, vars_):
        a = vars_[0]
        b = vars_[1]
        area = Rectangle(a, b)
        s = a * b
        p = area.rect_perimeter()
        s_test = (p * a - 2 * a ** 2) / 2
        assert s == s_test

    @pytest.mark.parametrize("vars_", argvalues=[(20, 30)])
    def test_2_2(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Rectangle(a, b)
        x = a * b
        assert num.rect_area() == x

    @pytest.mark.parametrize("vars_", argvalues=[(500, 100)])
    def test_2_3(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Rectangle(a, b)
        x = a + b
        assert num.rect_perimeter() != 0

    @pytest.mark.parametrize("vars_", argvalues=[(456, 230)])
    def test_2_4(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Rectangle(a, b)
        x = (a + b) * 2
        assert num.rect_perimeter() == x

    @pytest.mark.parametrize("vars_", argvalues=[(2, 4)])
    def test_2_5(self, vars_):
        a = vars_[0]
        b = vars_[1]
        d = math.sqrt((a ** 2) + (b ** 2))
        y = math.sqrt((d ** 2) - (b ** 2))
        num = Rectangle(y, b)
        assert a == int(y)

# Квадрат
    @pytest.mark.parametrize("vars_", argvalues=[(6, 8)])
    def test_3_1(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Square(a, b)
        x = a * b
        assert num.sq_area() == x

    @pytest.mark.parametrize("vars_", argvalues=[(20, 40)])
    def test_3_2(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Square(a, b)
        s = a * b
        p = num.sq_perimeter()
        s_test = (p * a - 2 * a ** 2) / 2
        assert s == s_test

    @pytest.mark.parametrize("vars_", argvalues=[(500, 100)])
    def test_3_3(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Square(a, b)
        x = a + b
        assert num.sq_perimeter() != 0

    @pytest.mark.parametrize("vars_", argvalues=[(456, 230)])
    def test_3_4(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Square(a, b)
        x = (a + b) * 2
        assert num.sq_perimeter() == x

    @pytest.mark.parametrize("vars_", argvalues=[(2, 4)])
    def test_3_5(self, vars_):
        a = vars_[0]
        b = vars_[1]
        d = math.sqrt((a ** 2) + (b ** 2))
        y = math.sqrt((d ** 2) - (b ** 2))
        assert a == int(y)

# Круг
    @pytest.mark.parametrize("vars_", argvalues=[3])
    def test_4_1(self, vars_):
        a = vars_
        print(a)
        num = Circle(a)
        x = math.pi * a ** 2
        assert num.c_area() == x

    @pytest.mark.parametrize("vars_", argvalues=[3])
    def test_4_2(self, vars_):
        a = vars_
        print(a)
        num = Circle(a)
        x = math.pi * a ** 2
        assert num.c_area() != 0

    @pytest.mark.parametrize("vars_", argvalues=[15])
    def test_4_3(self, vars_):
        a = vars_
        num = Circle(a)
        x = math.pi * a * 2
        assert num.c_perimeter() == x

    @pytest.mark.parametrize("vars_", argvalues=[75])
    def test_4_4(self, vars_):
        a = vars_
        num = Circle(a)
        x = math.pi * a * 2
        assert num.c_perimeter() != 0

    @pytest.mark.parametrize("vars_", argvalues=[32])
    def test_4_5(self, vars_):
        a = vars_
        d = 2 * a
        c = math.pi * d
        num = Circle(a)
        x = num.c_perimeter()
        assert x == c