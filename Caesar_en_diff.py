# Шифр Цезаря со сдвигом вправо
n = int(input())
s = input() # Вводимая строка
ss = ""
for i in range(len(s)):
    if (ord(s[i])+n)>122:
        a = n - (123-ord(s[i]))
        ss += chr(96+a)
    else:
        ss += chr(ord(s[i])+n)
print(ss)