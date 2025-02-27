class Scales:

    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n

    def get_result(self):
        if self.left == self.right:
            return "Весы в равновесии"
        elif self.left > self.right:
            return "Левая чаша тяжелее"
        else:
            return "Правая чаша тяжелее"


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())


scales = Scales()

scales.add_right(1)
scales.add_left(2)

print(scales.get_result())


scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())