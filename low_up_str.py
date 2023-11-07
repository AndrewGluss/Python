def lowUp(stroka):
	if stroka[0] == '!':
		stroka = stroka.upper()
	elif stroka[0] != '!':
		stroka = stroka.lower()
	
	for i in stroka:
		if i in '!@#%':
			stroka = stroka.replace(i, '')
	
	return stroka
	

stroka = input()
while stroka:
	print(lowUp(stroka))
	stroka = input()