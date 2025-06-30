import calendar
from datetime import date

def third_thursday_month(year):
    thursdays = []
    for i in range(1, 13):
        days_month = calendar.monthcalendar(year, i)
        thursdays_months = []
        for weeks in days_month:
            for days in weeks:
                if days != 0:
                    if calendar.weekday(year, i, days) == 3:
                        thursdays_months.append(date(year, i, days))
        thursdays.append(thursdays_months)

    for months in thursdays:
        print(months[2].strftime('%d-%m-%Y'), end='\n')

third_thursday_month(2021)