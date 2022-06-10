''' модуль turtle'''
'''Система черепашьей графики не встроена в интерпретатор Python и хранится в модуле turtle'''
import turtle
# turtle.showturtle() - появляется графическое окно с черепашкой
#по умолчанию черепашка смотрит на восток
# turtle.forward(n)-перемещение черепашки на n пикселей вперед
# turtle.backward(n)-перемещение черепашки на n пикселей назад
# turtle.right(angle)-поворачивает черепашку вправо на angle градусов
# turtle.left(angle)-поворачивает черепашку влево на angle градусов
# turtle.setheading()-применяется для установки углового направления черепашки с заданным углом
# turtle.heading()-возвращает текущее угловое направление черепашки
# turtle.shape()-изменение формы черепашки: square, arrow, circle, turtle, triangle, classic

''' рисуем прямоугольник со сторонами
import turtle
def rectangle(wigth, heigth):
  turtle.forward(wigth)
  turtle.right(90)
  
  turtle.forward(heigth)
  turtle.right(90)
  
  turtle.forward(wigth)
  turtle.right(90)
  
  turtle.forward(heigth)
  turtle.right(90)

rectangle(50,70)
'''
''' рисует правильынй треугольник
import turtle
def triangle(side):
  turtle.left(120)
  turtle.forward(side)
  
  turtle.left(120)
  turtle.forward(side)
  
  turtle.left(120)
  turtle.forward(side)
  
triangle(50)
'''
