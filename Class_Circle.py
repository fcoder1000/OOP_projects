from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def aria(self):
        return (self.radius ** 2) * pi

    def perimeter(self):
        return (2 * self.radius) * pi

circle = Circle(3)
print(circle.perimeter())
print(circle.aria())