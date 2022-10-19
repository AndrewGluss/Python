def create_phone_number(numbers):
    '''Функция create_phone_number принимает на вход список цифр о 1 до 9 в определенном порядке,
    и возвращает номер телефона
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) => "(123) 456-7890"
    create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) => "(111) 111-1111"
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) => "(123) 456-7890"
    create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) => "(023) 056-0890"
    create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) => "(000) 000-0000"
    '''
    code = "".join([str(i) for i in numbers[0:3]])
    part_1 = "".join([str(i) for i in numbers[3:6]])
    part_2 = "".join([str(i) for i in numbers[6:]])
    phone_number = "("+code+") "+part_1+"-"+part_2
    return phone_number


#    return '({}) {}-{}'.format(code, part_1, part_2)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))