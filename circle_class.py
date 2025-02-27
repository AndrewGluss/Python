from math import pi
class Circle:

    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = 2 * self.radius
        self.area = pi * (self.radius ** 2)


class Circle2:

    def __init__(self, radius):
        self._radius = radius
        self._diameter = self._radius * 2
        self._area = pi * (self._radius ** 2)

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area

circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)



circle2 = Circle2(1)

print(circle2.get_radius())
print(circle2.get_diameter())
print(round(circle2.get_area()))