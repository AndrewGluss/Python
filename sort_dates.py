from datetime import date

n = int(input())
dates = list()
for i in range(n):
    dates.append(date.fromisoformat(input()))
for dat in sorted(dates):
    print(dat.strftime("%d/%m/%Y"))