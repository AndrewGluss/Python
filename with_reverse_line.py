'''Есть файл data.txt с одной строкой. Напишите программу, которая выводит на экран эту строку в обратном порядке'''
with open("data.txt", encoding='utf-8') as file:
    lines = file.readlines()
    lines1 = lines[::-1]
    for line in lines1:
        print(line.strip())