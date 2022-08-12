import string

def lenght(stroka):
    stroka = stroka.upper()
    if stroka.isalpha():
        return len(stroka)
    else:
        #print(lenght(stroka))
        summ = 0  # сумма чисел в строке
        count = 0  # счетчик букв в строке
        stroka1 = stroka
        for i in stroka1:
            if i in string.ascii_letters:
                count += 1
                stroka1 = stroka1.replace(i, ' ')
        list1 = stroka1.split()
        for i in list1:
            summ += int(i)
        x = count - len(list1) + summ  # count - len(list1) - узнаем сколько букв не надо умножать на числа
        return x

#stroka = input()

lenght('A4B3')

