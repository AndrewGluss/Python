from datetime import datetime

def num_of_sundays(year):
    start = datetime(year=year, month=1, day=1)
    end = start.replace(month=12, day=31)
    count = 0
    for i in range(start.toordinal(), end.toordinal()+1):
        if datetime.strftime(datetime.fromordinal(i), "%A") == "Sunday":
            count += 1
    return count



year = int(input())
print(num_of_sundays(year))