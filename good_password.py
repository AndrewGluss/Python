'''Хороший пароль по условиям этой задачи состоит как минимум из 77 символов,
содержит хотя бы одну цифру, заглавную и строчную букву. 
Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.'''
password = input()
if len(password)>=7:
    if all([any(list(map(lambda x: True if x.islower() else False, password))), any(list(map(lambda x: True if x.isupper() else False, password))), any(list(map(lambda x: True if x.isdigit() else False, password)))]):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
