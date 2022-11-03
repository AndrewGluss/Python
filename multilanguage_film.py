'''
На вход программе в первой строке подается число nn — количество людей, которых донимает режиссер.
В каждой из следующих nn строк через запятую и пробел указывается список языков, которые знает человек.
Программа должна вывести список языков для сериала в лексикографическом порядке. Если такой список составить нельзя, необходимо вывести текст:
Сериал снять не удастся
'''
n = int(input())
multilang = []
for i in range(n):
    languages = set([j for j in input().split(', ')])
    multilang.append(languages)
film = multilang[0]
for i in range(1, len(multilang)):
    film &= multilang[i]
    # print(film)
if len(film) == 0:
    print('Сериал снять не удастся')
else:
    print(*film, sep=", ")

