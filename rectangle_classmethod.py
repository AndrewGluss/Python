class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @classmethod
    def square(cls, side):
        return cls(side, side)

rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)

rectangle = Rectangle.square(5)

print(rectangle.length)
print(rectangle.width)

