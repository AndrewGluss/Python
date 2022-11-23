from datetime import datetime

def fill_up_missing_dates(dates):
    dates_dt = sorted([datetime.strptime(i, "%d.%m.%Y") for i in dates])
    full_dates = []
    for i in range(dates_dt[0].toordinal(), dates_dt[-1].toordinal()+1):
        full_dates.append(datetime.strftime(datetime.fromordinal(i).date(), "%d.%m.%Y"))
    return full_dates

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))



