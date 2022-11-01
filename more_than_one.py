def more_that_one(numbs):
    '''Функция приниает на вход строку чисел,
    и возвращает числа в порядке возрастания, которые встречаются больше одного раза.
    '''
    numbers = [int(i) for i in numbs.split(" ")]
    dict_numbs = dict()
    for num in numbers:
        dict_numbs[num] = dict_numbs.setdefault(num, 0) + 1

    for key,value in sorted(dict_numbs.items()):
        if value > 1:
            print(key, end=' ')


more_that_one("4 8 0 3 4 2 0 3")