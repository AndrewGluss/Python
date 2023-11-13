def filter(func, seq):
	list1 = [i for i in seq if func(i)]
	return list1
	
func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
	print(x)