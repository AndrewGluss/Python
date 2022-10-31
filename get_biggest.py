def get_biggest(numbers):
    '''Функция приниает на вход список чисел, и возвращает наибольшее число, которое можно составить из чисел списка
    иначе если список пустой вернуть -1
    get_biggest([]) -> -1
    get_biggest([0, 0, 0, 0, 0, 0]) -> 0
    get_biggest([1, 2, 3]) -> 321
    get_biggest([953, 9534]) -> 9539534
    '''
    if len(numbers) > 0:
        maxDigit = len(str(max(numbers)))
        sorted_numbers = sorted(numbers, key=lambda x: str(x)*maxDigit, reverse=True)
        a = [str(i) for i in sorted_numbers]
        return int(''.join(a))
    return -1