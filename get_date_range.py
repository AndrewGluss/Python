from datetime import date

def get_date_range(date1, date2):
    '''Функция принимает на вход две даты, где первая дата - начала периода, а вторая - конец, и возвращает список дат внутри периода
    '''
    dates = list()
    for i in range(date1.toordinal(), date2.toordinal()+1):
        dates.append(date.fromordinal(i))
    return dates

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 6)

print(get_date_range(date1, date2))

date1 = date(2019, 6, 5)
date2 = date(2022, 6, 6)
print(len(get_date_range(date1, date2)))