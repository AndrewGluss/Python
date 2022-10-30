def sq_in_rect(lng, wdth):
    '''Функ принимает на вход длину и ширину прямоугольника. и возвращает список квадратов умещающщихся в прямоугольнике.
    sq_in_rect(5,3) -> [3,2,1,1] # первый квадрат 3*3, второй 2*2, третий и четвертый 1*1
    '''
    square = []
    if lng == wdth:
        square = [lng]
        return square
    else:
        if lng > wdth:
            square += [wdth] + sq_in_rect(lng-wdth, wdth)
        else:
            square += [lng] + sq_in_rect(wdth-lng, lng)
    return square
