# Шифр Цезаря со сдвигом влево
n = int(input()) # сдвиг
s = input() # Вводимая строка
ss = ""
for i in range(len(s)):
    if (ord(s[i])-n)<97:
        a = n - (ord(s[i])-97)
        ss += chr(123-a)
    else:
        ss += chr(ord(s[i])-n)
print(ss)