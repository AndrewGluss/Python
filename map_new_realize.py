def map(func, seq):
	list1 = []
	for i in seq:
		list1.append(func(i))
	
	return list1
	
func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
	print(x)