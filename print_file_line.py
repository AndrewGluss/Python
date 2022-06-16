'''Программа выводит содержимое файла, имя которого нужно ввести'''
file_name = input("Введите имя файла: ")
file = open(file_name, 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()