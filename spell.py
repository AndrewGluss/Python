def spell(*words):
    """Принимает список слов words и возвращает словарь, где ключ - первая буква слова,
    а значение - максимальная длина слова на эту букву
    """
    spell_dict = dict()
    if len(words) > 0:
        # w_key = words[0][0]
        # w_value = len(words[0])
        spell_dict[words[0][0].lower()] = len(words[0])
        for i in range(1, len(words)):
            print(spell_dict)
            if words[i][0].lower() in spell_dict and len(words[i]) > spell_dict[words[i][0].lower()]:
                spell_dict[words[i][0].lower()] = len(words[i])
            elif words[i][0].lower() not in spell_dict:
                spell_dict[words[i][0].lower()] = len(words[i])
        return spell_dict
    return spell_dict

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))