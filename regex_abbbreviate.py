from re import findall

def abbreviate(text):

    pattern = r'\b([a-zA-z])|([A-Z])'

    x = findall(pattern, text)
    #print(x)
    abbreviature = ''
    for i in x:
        for j in i:
            if j != '':
               abbreviature += j
    return abbreviature.upper()


print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))