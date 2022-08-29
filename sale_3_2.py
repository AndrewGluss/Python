t = int(input())
for i in range(t):
    dict1 = dict()
    summ = 0
    n = int(input())
    numbs = [int(j) for j in input().split()]
    for k in numbs:
        dict1[k] = dict1.setdefault(k,0) + 1
    print(dict1)
    for num, col in dict1.items():
        if col >=3:
            summ += num*(col - (col//3))
        else:
            summ += num*col
    print(summ)