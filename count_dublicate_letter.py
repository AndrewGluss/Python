def dublicate_count(text):
    """
    Функция принимает на вход строку (текст)
    и возвращает число - количество дублирующих букв в строке
    dublicate_count('aabBcde') == 2
    dublicate_count('abcde') == 0
    dublicate_count('aA11') == 2
    dublicate_count('AAdc') == 1

    """
    count_dublicate = 0
    letter_dict = dict()
    for i in text.lower():
        letter_dict[i] = letter_dict.setdefault(i,0) + 1
    for letter in letter_dict:
        if letter_dict[letter] > 1:
            count_dublicate += 1
    return count_dublicate

    # return len([c for c in set(s.lower()) if s.lower().count(c)>1])
