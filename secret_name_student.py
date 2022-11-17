def tricky_cipher(student):
    """Функция приниает на вход кортеж student = ('surname','name','second name','day','month','year'), а возвращает секретный шифр полученный определенны образом:
        Подсчитывается количество различных символов в ФИО (регистр важен, А и а — разные символы).
        Берётся сумма цифр в дне и месяце рождения, умноженная на 64.
        Для первой (по позиции в слове) буквы фамилии определяется её номер в алфавите (в 1-индексации), умноженный на 256 (регистр буквы не важен).
        Полученные числа суммируются.
        Результат переводится в 16-чную систему счисления (в верхнем регистре).
        У результата сохраняются только 3 младших разряда (если значимых разрядов меньше, то шифр дополняется до 3-х разрядов ведущими нулями).
    """
    surname = student[0]
    ind = alph.index(surname[0])
    # print("Позиция первой буквы фамилии",ind)
    uniq_letter = set("".join(student[:3]))
    # print(uniq_letter, len(uniq_letter))
    uniq_date = "".join(student[3:5])
    count = 0
    for i in uniq_date:
        count += int(i)
    # print(count)
    result = len(uniq_letter) + count * 64 + ind * 256
    # print("итоговое значение шифра: ", result)
    # print("шестнадцатиричное предстваление: ", hex(result)[-3:].upper())
    return hex(result)[-3:].upper()


n = int(input())
students = [0]*n
alph = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
secret = []
for i in range(n):
    student = input().split(',')
    secret[i] = tricky_cipher(tuple(student))
print(' '.join(secret))


'''
input
2
Volozh,Arcady,Yurievich,11,2,1964
Segalovich,Ilya,Valentinovich,13,9,1964

output
710 64F
'''
