'''Есть файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.
Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).'''
with open("numbers.txt", encoding='utf-8') as file:
    numb = file.readlines()
    numb1 = []
    for line in numb:
        numb1.append(line.strip().split())
    for numbs in numb1:
        count = 0
        for i in numbs:
            count += int(i)
        print(count)