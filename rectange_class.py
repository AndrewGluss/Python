class Rectangle:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_perimeter(self):
        return 2 * (self._length + self._width)

    def get_area(self):
        return self._length * self._width

    length = property(get_length, set_length)
    width = property(get_width, set_width)
    perimeter = property(get_perimeter)
    area = property(get_area)

rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)


rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)