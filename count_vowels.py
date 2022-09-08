def count_vowels(sentence):
    """
    Функция паринимает на вход строку в нижнем регистре
    и возвращает количество гласных букв в строке.
    """
    count = 0
    for i in sentence:
        if i in 'aeiouAEIOU':
            count += 1
    return count

