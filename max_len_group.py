def max_len_group(numb):
    '''Функция приниает на вход число и возвращает максимальное количество чисел, чья сумма цифр каждого числа одинакова
    '''
    numbers = [i for i in range(1, numb + 1)]
    sum_dict = dict()
    for i in range(len(numbers)):
        s = numbers[i]
        for j in range(len(numbers)):
            sumNum = 0
            x = numbers[j]
            while x > 0:
                sumNum += x%10
                x = x//10
            if sumNum == s:
                sum_dict[s] = sum_dict.setdefault(s, []) + [numbers[j]]
    max_len = []
    for value in sum_dict.values():
        max_len.append(len(value))
    return max(max_len)

print(max_len_group(1337))