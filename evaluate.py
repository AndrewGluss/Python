'''Написать функцию evaluate(), которая принимает на вход строку из коэффициентов и целое число, а на выходе результат многочлена'''
from functools import *
def evaluate(coefficients, x):
	lens = [i for i in range(len(coefficients))]
	x1 = list(map(lambda p,r: (x**p)*r, lens[::-1],coefficients))
	return reduce(lambda x,y: x+y,x1,0)
	
coefficients = [int(i) for i in input().split()]
x = int(input())

print(evaluate(coefficients, x))

