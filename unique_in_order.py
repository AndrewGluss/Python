def unique_in_order(iterable):
    """
    Функция принимает на вход итерируемый объект в котором дублируются элементы,
    и возвращает список элементов в том же порядке, но без дублирования
    unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1,2,2,3,3]) == [1,2,3]
    """
    unique_list = []
    if len(iterable) > 0:
        current_unique = iterable[0]
        unique_list.append(current_unique)
        for i in iterable:
            if i != current_unique:
                unique_list.append(i)
                current_unique = i
        return unique_list
    return unique_list

