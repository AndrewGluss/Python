from re import split, escape

def multiple_split(text, delimeters):

    pattern = '|'.join(map(escape, delimeters))

    data = split(pattern, text)

    return data


print(multiple_split('beegeek-python.stepik', ['.', '-']))
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
