def index_of_nearest(numbers, number):
    """
    Функция принимает на вход список чисел numbers и число number
    и возвращает индекс ближайшего числа из списка numbers к числу number
    """
    if len(numbers) > 0:
        min_diff = []
        for num in numbers:
            min_d = abs(number-num)
            min_diff.append(min_d)
        x = min(min_diff)
        ind_min = min_diff.index(x)
        return ind_min
    else:
        return -1

print(index_of_nearest([7, 5, 4, 4, 3], 4))