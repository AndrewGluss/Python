import datetime

def good_period(pice):
    """
    Функция проверяет на корректность временного отрезка
    и возвращает True, когда отрезок корректный и False, когда некорректный.
    """
    try:
        time1 = datetime.datetime.strptime(pice[0], '%H:%M:%S')
        time2 = datetime.datetime.strptime(pice[1], '%H:%M:%S')
        if time1 <= time2:
            return True
        return False
    except ValueError:
        return False

def not_cross(list_period):
    """
    Функция проверяет на пересечение периодов
    и возвращает True, когда все промежутки не паресекаются
    и возвращает False, когда есть хотябы одно пересечение.
    """
    cross_list = []
    for i in range(len(list_period)):
        for j in range(i+1, len(list_period)):
            if good_period(list_period[i]) and good_period(list_period[j]):
                time1 = datetime.datetime.strptime(list_period[i][0], '%H:%M:%S')
                time2 = datetime.datetime.strptime(list_period[i][1], '%H:%M:%S')
                time3 = datetime.datetime.strptime(list_period[j][0], '%H:%M:%S')
                time4 = datetime.datetime.strptime(list_period[j][1], '%H:%M:%S')
                if time2 < time3 or time4 < time1:
                    cross_list.append(True)
                else:
                    cross_list.append(False)
                    break
            else:
                cross_list.append(False)
                break
    return all(cross_list)


t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    list_period = [0]*n # список, понадобится для проверки пересечения
    for j in range(n):
        period = [k for k in input().split('-')]
        if good_period(period): # если промежуток времени правильный, увеличиваем счетчик на единицу
            count += 1
        list_period[j] = period

    if count == n and not_cross(sorted(list_period, key = lambda x: x[0])):  # если счетчик равен количеству промежутков и пересечений нет
        print("YES")
    else:
        print("NO")