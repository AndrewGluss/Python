'''
На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков.
В следующих nn строках перечислены сами ящики в порядке выдачи, по одному на строке.
На следующей строке задано целое неотрицательное число m — количество новых сотрудников, которым нужно раздать корпоративные ящики.
Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Sample Input
2
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3
timyr-guev
timyr-guev
anri-tabuev

Sample Output
timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
'''
n = int(input())
existEmail = []
for i in range(n):
    existEmail.append(input())
m = int(input())
for i in range(m):
    count = 0
    name = input()
    new_email = name+"@beegeek.bzz"
    while new_email in existEmail:
        # print(existEmail)
        # print("занимай новый")
        count += 1
        new_email = name + str(count) + "@beegeek.bzz"
    if count > 0:
        new_email = name+str(count)+"@beegeek.bzz"
    existEmail.append(new_email)
    print(new_email)