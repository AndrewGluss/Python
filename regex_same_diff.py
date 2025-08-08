from re import findall, IGNORECASE

word = input()
stroka = input()


#print(word[:-2])
x = fr'\b({word[:-2]})[zs]e\b'

y = findall(x, stroka, flags=IGNORECASE)

print(len(y))