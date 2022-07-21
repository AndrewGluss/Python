'''Напишите функцию func, используя синтаксис анонимных функций,
которая принимает целочисленный аргумент и возвращает значение True,
если он делится без остатка на 19 или на 13 и False в противном случае.'''

func1 = lambda x: True if x%19==0 or x%13==0 else False
#print(func1(19))
#print(func1(13))
#print(func1(20))
#print(func1(15))
#print(func1(247))

'''Напишите функцию func, используя синтаксис анонимных функций,
которая принимает строковый аргумент и возвращает значение True,
если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) и False в противном случае.'''

func2 = lambda x: True if x[0].lower()=='a' and x[0].lower()==x[-1].lower() else False
#print(func('abcd'))
#print(func('bcda'))
#print(func('abcda'))
#print(func('Abcd'))
#print(func('bcdA'))
#print(func('abcdA'))

'''Напишите функцию is_non_negative_num, используя синтаксис анонимных функций,
которая принимает строковый аргумент и возвращает значение True,
если переданный аргумент является неотрицательным числом (целым или вещественным) и False в противном случае.'''

is_non_negative_num = lambda x: True if x.replace('.', '').isdigit() and x.count('.') < 2 else False

#print(is_non_negative_num('10.34ab'))
#print(is_non_negative_num('10.45'))
#print(is_non_negative_num('-18'))
#print(is_non_negative_num('-34.67'))
#print(is_non_negative_num('987'))
#print(is_non_negative_num('abcd'))
#print(is_non_negative_num('123.122.12'))
#print(is_non_negative_num('123.122'))

'''Напишите функцию is_num, используя синтаксис анонимных функций,
которая принимает строковый аргумент и возвращает значение True,
если переданный аргумент является числом (целым или вещественным) и False в противном случае.'''

is_num = lambda x: True if x.replace('.', '').isdigit() and x.count('.') < 2 or x[0]=='-' and x[1:].replace('.', '').isdigit() and x[1:].count('.') < 2 else False

#print(is_num('10.34ab'))
#print(is_num('10.45'))
#print(is_num('-18'))
#print(is_num('-34.67'))
#print(is_num('987'))
#print(is_num('abcd'))
#print(is_num('123.122.12'))
#print(is_num('-123.122'))
#print(is_num('--13.2'))
