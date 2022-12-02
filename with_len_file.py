'''На вход программе подается строка текста с именем текстового файла.
Напишите программу для вывода на экран количества строк данного файла.'''

name = input()
with open(name, encoding='utf-8') as files:
    fileList = [file.strip() for file in files.readlines()]
    print(len(fileList))
