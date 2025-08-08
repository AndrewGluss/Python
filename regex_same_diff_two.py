from re import findall, IGNORECASE

word = input()
stroka = input()


#print(word[:-3])
x = fr'\b({word[:-3]})o[u]?r\b'

y = findall(x, stroka, flags=IGNORECASE)

print(len(y))