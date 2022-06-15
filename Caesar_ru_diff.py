# Шифр Цезаря со сдвигом влево
n = int(input()) # сдвиг
s = input() # Вводимая строка
ss = ""
for i in range(len(s)):
    if (ord(s[i])+n)<1072:
        a = n - (ord(s[i])-1072)
        ss += chr(1103-a)
    else:
        ss += chr(ord(s[i])-n)
print(ss)
