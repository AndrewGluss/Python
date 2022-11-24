from datetime import datetime

def between_days(list_dt):
    btw_d = []
    for i in range(0, len(list_dt)-1):
        btw_d.append(abs((list_dt[i+1] - list_dt[i]).days))
    print(btw_d)

list_dt = [datetime.strptime(i, "%d.%m.%Y").date() for i in input().split(" ")]
# print(list_dt)
between_days(list_dt)