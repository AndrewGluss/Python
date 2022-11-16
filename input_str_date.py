from datetime import date, time

while True:
    try:
        day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ: ').split('.')

        my_date = date(int(year), int(month), int(day))

        print('Введена корректная дата:', my_date)
        break
    except:    # перехватываем ошибку типа ValueError
        print('Введенная дата не является корректной, попробуйте еще раз')