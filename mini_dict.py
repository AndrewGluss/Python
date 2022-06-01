mini_dict = {}
n = int(input())
list1 = []
for i in range(n):
    #print(i)
    list1.append(input().split(": "))
m = int(input())
list2 = [input() for i in range(int(input()))]
#print(list2)
for i in range(len(list_1)):
	mini_dict[list_1[i][0].lower()] = list_1[i][1]
#print(mini_dict)
for i in list_2:
    print(mini_dict.get(i.lower(), "Не найдено"))