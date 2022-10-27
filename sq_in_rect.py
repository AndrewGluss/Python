def sq_in_rect(lng, wdth):
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
