list1 = [int(i) for i in input().split()]
list2= [i for i in range(list1[0], list1[1], list1[2])]
#print(list2)
for i in map(lambda x: x**2 if x%2!= 0 else -x,list2):
	print(i)
