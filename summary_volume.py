'''
Программа считывает текстовый файлб содержащий информацию о файлах.
Каждая строка файла содержит три значения, разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:
    cant-help-myself.mp3 7 MB
    keep-yourself-alive.mp3 6 MB
    bones.mp3 5 MB
    ...
Программа группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и выводит полученные группы файлов, указывая для каждой ее общий объем.
Группы должны быть расположены в лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен
'''
with open("summary_volume_input.txt", encoding='utf-8') as files:
    fileList = [file.strip() for file in files.readlines()]
    fileDict = dict()
    for file in fileList:
        list1 = file.split(' ')
        name  = list1[0]
        volume = list1[1:]
        dot = name.index(".")
        ext = name[dot+1:]
        new_f = dict()
        new_f[name] = volume
        fileDict[ext] = fileDict.setdefault(ext, []) + [(name,volume)]

    # print(fileDict)
    for key, value in sorted(fileDict.items()):
        # key - расширение файла
        # value - список кортежей
        Summary = 0
        for i in sorted(value, key=lambda x: x[0]):
            # i - кортеж
            print(i[0])
            if i[1][1][0] == "M":
                Summary += int(i[1][0]) * 1024 * 1024
            elif i[1][1][0] == "K":
                Summary += int(i[1][0]) * 1024
            elif i[1][1][0] == "G":
                Summary += int(i[1][0]) * 1024 * 1024 * 1024
            else:
                Summary += int(i[1][0])
            # print(k)
        if Summary > 1024**3:
            Summary = str(round(Summary / 1024**3)) + " GB"
        elif 1024**3 > Summary > 1024**2:
            Summary = str(round(Summary / 1024**2)) + " MB"
        elif 1024**2 > Summary > 1024:
            Summary = str(round(Summary / 1024)) + " KB"
        else:
            Summary = str(Summary) + " B"
        print("----------")
        print("Summary:", Summary)
        print()

