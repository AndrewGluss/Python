def narcissistic(value):
    """
    Функция возвращает True если сумма цифр числа умноженных на их количество равна самому числу
    и возвращает False - если не равна.
    narcissistic(153) 1**3 + 5**3 + 3**3 = 153 -> True
    narcissistic(1652) 1**4 + 6**4 + 5**4 + 2**4 = 1938 -> False
    """
    value1 = value
    numbers = []
    summ = 0
    while value1>0:
        x = value1%10
        numbers.append(x)
        value1 = value1//10
    for number in numbers:
        summ += number**len(numbers)
    if summ == value:
        return True
    return False
