from datetime import date
def saturdays_between_two_dates(date1,date2):
    '''Функция принимает на вход две даты в произвольном порядке, и возвращает количество суббот в заданном периоде'''
    saturday = []
    if date2 < date1:
        date1, date2 = date2, date1
    for i in range(date1.toordinal(), date2.toordinal() + 1):
        if date.fromordinal(i).weekday() == 5:
            saturday.append(date.fromordinal(i))
    return len(saturday)

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))