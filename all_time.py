from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

count_minutes = timedelta(minutes=0)

for period in data:
    delta = datetime.strptime(period[1], "%H:%M") - datetime.strptime(period[0], "%H:%M")
    count_minutes += delta

print(int((count_minutes.total_seconds())//60))