def not_cross(list_period):
    """
    Функция проверяет на пересечение периодов
    и возвращает True, когда все промежутки не паресекаются
    и возвращает False, когда есть хотябы одно пересечение.
    """
    cross_list = []
    for i in range(len(list_period)):
        for j in range(i+1, len(list_period)):
            if (list_period[i][0] == list_period[j][1]) or (
                good_period([list_period[j][1],list_period[i][0]])==False) or (
                good_period([list_period[j][0],list_period[i][1]])==False) or (
                list_period[i][1] == list_period[j][0]
            ):
                cross_list.append(False)
            else:
                cross_list.append(True)
    return all(cross_list)

def good_period(pice):
    """
    Функция проверяет на корректность временного отрезка
    и возвращает True, когда отрезок корректный и False, когда некорректный.
    """
    pices = []
    for i in pice:
        times = i.split(':')
        pices.append(times)
    if (int(pices[0][0])<=int(pices[1][0]) and (0<=int(pices[0][0])<=23 and 0<=int(pices[1][0])<=23)) and (
        int(pices[0][1]) <= int(pices[1][1]) and (0 <= int(pices[0][1]) <= 59 and 0 <= int(pices[1][1]) <= 59)) and (
        int(pices[0][2]) <= int(pices[1][2]) and (0 <= int(pices[0][2]) <= 59 and 0 <= int(pices[1][2]) <= 59)):
        return True
    else:
        return False

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    list_period = [] # список, понадобится для проверки пересечения
    for j in range(n):
        # period = [[k for k in j.split(':')] for j in input().split('-')]
        # if int(period[0][0])<=int(period[0][0]) and int(period[0][1])<=int(period[0][1]) and int(period[0][2])<=int(period[0][2]):
        period = [k for k in input().split('-')]
        if good_period(period): # если промежуток времени правильный, увеличиваем счетчик на единицу
            count += 1
        list_period.append(period)
    # print(list_period)
    if count == n and not_cross(list_period):  # если счетчик равен количеству промежутков и пересечений нет
        print("YES")
    else:
        print("NO")