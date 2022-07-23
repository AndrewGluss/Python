'''Написать функцию generate_passwords(n,m), где n - количество генерированных паролей, m = длина паролей'''
import random
import string
def generate_password(length):
    basic = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789'
    c_b = 0
    c_s = 0
    c_d = 0
    new = random.sample(basic, m)
    while (c_b<1) or (c_s<1) or (c_d<1):
    	for i in new:
    		if i in 'abcdefghijkmnpqrstuvwxyz':
    			c_s+=1
    		if i in 'ABCDEFGHJKMNPQRSTUVWXYZ':
    			c_b+=1
    		if i in '23456789':
    			c_d+=1
    	if (c_b<1) or (c_s<1) or (c_d<1):
            new = random.sample(basic, m)
            c_b = 0
            c_s = 0
            c_d = 0
    new1= ''.join(new)
    return new1
    	

def generate_passwords(count, length):
    list_password = []
    for i in range(n):
    	list_password.append(generate_password(m))
    print(*list_password, sep = "\n")

n, m = int(input()), int(input())

generate_passwords(n,m)
