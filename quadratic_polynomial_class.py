from math import sqrt
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

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


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)



polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)