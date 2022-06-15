# Шифр Цезаря со сдвигом вправо
n = int(input()) # сдвиг
s = input() # Вводимая строка
ss = ""
for i in range(len(s)):
    if (ord(s[i])+n)>1104:
        a = n - (1104-ord(s[i]))
        ss += chr(1071+a)
    else:
        ss += chr(ord(s[i])+n)
print(ss)