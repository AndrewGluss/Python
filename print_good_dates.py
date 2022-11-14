from datetime import date

def print_good_dates(dates):
    idol = {"born": 1992, "age": 29}
    for dat in sorted(dates):
        if dat.year == idol["born"] and dat.month+dat.day == idol["age"]:
            print(dat.strftime("%B %d, %Y"))


dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)