def devide_string(value):
    '''

    '''
    result = list()
    if len(value) %2 != 0:
        value += "_"
    for i in range(0, len(value), 2):
        result.append(value[i:i+2])
    return result

print(devide_string('abcdef'))