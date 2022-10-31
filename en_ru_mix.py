def en_ru_mix(a, b, c):
    '''Функция принимает на вход три символа и возвращает:
    ru - если все 3 символа на кириллице
    en - если все 3 символа на латинице
    mix - и такой символ и другой
    '''
    sameEN = "AaBCcEeHKMOoPpTXxy"
    sameRU = "АаВСсЕеНКМОоРрТХху"
    if a in sameRU and b in sameRU and c in sameRU:
        return 'ru'
    elif a in sameEN and b in sameEN and c in sameEN:
        return 'en'
    return 'mix'

print(en_ru_mix('Р', 'О', 'А'))