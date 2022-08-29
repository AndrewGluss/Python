def series_day_work(works):
    """
    Функция возвращает True, если в выполнении каждой задачи не было перерывов
    и False если серия дней на выполнение одной задачи прервалась
    """
    works_copy = works
    dict_works = dict() # создаем словарь в котором ключ - задача, значение - количество потраченных дней без перерыва
    current_task = works_copy[0] # текущая задача
    dict_works[current_task] = 1
    sum_days = 0 # суммарное количество дней
    for i in range(1, len(works_copy)):
        # если задача равна текущей и есть в словаре
        if works_copy[i] == current_task and works_copy[i] in dict_works:
            # прибавляем к серии дней 1
            dict_works[current_task] = dict_works.setdefault(current_task, 0) + 1
        # если задача не равна текущей и её нет в словаре
        elif works_copy[i] != current_task and works_copy[i] not in dict_works:
            # задачу текущей
            current_task = works_copy[i]
            # добавляем в словарь
            dict_works[current_task] = dict_works.setdefault(current_task, 0) + 1
        # если задача не равна текущей и присутсвует в словаре, то серия прервалась
        elif works_copy[i] != current_task and works_copy[i] in dict_works:
            break
    for values in dict_works.values():
        sum_days += values
    if sum_days == len(works_copy):
        return True
    else:
        return False


t = int(input())  # вводим количество наборов
for i in range(t):
    n = int(input())  # вводим количество дней в отчете
    works = [int(j) for j in input().split()]  # список задач которые решались за n-дней
    if series_day_work(works):
        print("YES")
    else:
        print("NO")