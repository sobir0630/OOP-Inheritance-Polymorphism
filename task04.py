import math

class Shape:
    def area(self):
        return "Yuza hisoblash formulasi aniqlanmagan."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

print(f"Doira yuzi: {circle.area()}")
print(f"Togri tortburchak yuzi: {rectangle.area()}")
print(f"Uchburchak yuzi: {triangle.area()}")
