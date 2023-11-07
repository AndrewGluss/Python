def avg_func(list1):
	return round(sum(list1) / len(list1), 2)

list1 = [int(i) for i in input().split()]	
while list1:
	print(avg_func(list1))
	list1 = [int(i) for i in input().split()]
	