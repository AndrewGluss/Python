from datetime import date
def get_min_max(dates):
    '''
    Функция принимает на вход список дат, и возвращает кортеж из инимальной и аксимальной дат списка.
    Если список пустой, то возвращает пустой кортеж
    '''
    if len(dates) == 0:
        return tuple(dates)
    else:
        return (min(dates),max(dates))

dates1 = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]

print(get_min_max(dates1))
print(get_min_max([]))

dates2 = [date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5)]

print(get_min_max(dates2))

dates3 = [date(1999, 9, 9)]

print(get_min_max(dates3))