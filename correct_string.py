stroka = input()

flag = False

if 'i' not in stroka and 'e' not in stroka:
	if 'a' in stroka or 'o' in stroka:
		flag = True

print(flag)