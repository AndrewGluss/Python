def choose_plural(amount, declensions):
    """
    Функция принимает на вход число amount - количество, и declensions - кортеж из трех вариантов склонения существительного
    и возвращает строку из amount и правильного склонения существительного
    print(choose_plural(21, ('пример', 'примера', 'примеров')))
    21 пример
    """
    if str(amount)[-1] in ['0','5','6','7','8','9'] or str(amount)[-1] in ['1','2','3','4'] and str(amount)[-2] == '1':
        return str(amount) + " " + declensions[2]
    elif str(amount)[-1] in ['2','3','4']:
        return str(amount) + " " + declensions[1]
    return str(amount) + " " + declensions[0]