from math import sqrt


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iter):
        return cls(iter[0], iter[1], iter[2])

    @classmethod
    def from_str(cls, text):
        x = text.split()
        return cls(float(x[0]), float(x[1]), float(x[2]))

    @property
    def x1(self):
        if (self.b ** 2) - (4 * self.a * self.c) < 0:
            return None
        else:
            return (-self.b - sqrt((self.b ** 2) - (4 * self.a * self.c))) / (2 * self.a)

    @property
    def x2(self):
        if (self.b ** 2) - (4 * self.a * self.c) < 0:
            return None
        else:
            return (-self.b + sqrt((self.b ** 2) - (4 * self.a * self.c))) / (2 * self.a)

    @property
    def coefficients(self):
        return tuple([self.a, self.b, self.c])

    @coefficients.setter
    def coefficients(self, coeffs):
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.c = coeffs[2]

    @property
    def view(self):
        return f"{self.a}x^2 + {self.b}x + {self.c}".replace('+ -', '- ')


polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)


polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)


polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
