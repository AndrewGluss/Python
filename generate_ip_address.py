'''Программа генерирует корректный ip в формате str'''
import random# подключаем библиотеку random
def generate_ip():
    numbers = [str(i) for i in range(0, 256)]# создаем список из чисел от 0 до 255 включительно в формате str
    ip = ".".join(random.sample(numbers, 4))# получаем строчку из 4 случайных чисел списка numbers с помощью random.sample
    return ip# возвращаем строчку
generate_ip()