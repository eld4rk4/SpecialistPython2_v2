class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance():
    """
    Расстояние между двумя точками
    """


# Дано две точки на координатной плоскости
points1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
a=point2.x-points1.x
b=point2.y-points1.y
from math import sqrt
c=sqrt(a*a+b*b)
# TODO: your core here...

print("Расстояние между точками = ", a,b,c)
