from datetime import datetime, timedelta

def schedule(time_dt):
    days = []
    now = time_dt
    days.append(now.date())
    n = 1
    while n < 10:
        now = now + timedelta(days=n+1)
        days.append(now.date())
        #print(now.date().strftime("%d.%m.%Y"))
        #print('n = ', n)
        n += 1
    print(*days, sep='\n')

time_dt = datetime.strptime(input(), "%d.%m.%Y")
# print(time_dt.date())
schedule(time_dt)