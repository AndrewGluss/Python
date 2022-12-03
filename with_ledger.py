'''Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц.
На каждой строке файла указано, сколько клиент заплатил за товар, в долларах (целое число):
    $47
    $100
    $60
    $12
    $8
    ...
Напишите программу для подсчета суммарной месячной выручки фирмы.'''

with open("ledger.txt", encoding='utf-8') as files:
    fileList = [file.strip() for file in files.readlines()]
    full_price = 0
    for i in fileList:
        full_price += int(i[1:])
    print("$"+str(full_price))