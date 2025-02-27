class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


circle = Circle(5)

print(circle.radius)

circle = Circle.from_diameter(10)

print(circle.radius)

