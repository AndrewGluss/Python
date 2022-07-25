'''На вход программе подаются три строки текста с вещественными числами,
значениями абсцисс (x), ординат (y) и аппликат (z) точек трехмерного пространства.
Напишите программу для проверки расположения всех точек с введенными координатами внутри
либо на поверхности шара с центром в начале координат и радиусом R = 2.

Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.
Примечание 2. Уравнение поверхности шара (сферы) имеет вид x^2+y^2+z^2 = R^2x 
Примечание 3. Для решения задачи используйте встроенные функции all() и zip().
Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков.'''
from decimal import *
abscissas = [i for i in input().split()]
ordinates = [i for i in input().split()]
applicates = [i for i in input().split()]
R = 2
in_ball = []
for x,y,z in zip(abscissas,ordinates,applicates):
    if (Decimal(x))**2 + (Decimal(y))**2 + (Decimal(z))**2 <= R**2:
        in_ball.append(True)
    else:
        in_ball.append(False)
print(all(in_ball))
#print(abscissas)
#print(ordinates)
#print(applicates)
