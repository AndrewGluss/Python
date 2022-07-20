<<<<<<< HEAD
import random
with open('E:/first_names.txt') as names, open('E:/last_names.txt') as surnames:
    name_list = [line.strip() for line in names.readlines()]
    surname_list = [line.strip() for line in surnames.readlines()]
    #print(name_list)
    #print(surname_list)
    for i in range(3):
        j = random.randint(0,len(name_list))
        k = random.randint(0,len(surname_list))
=======
import random
with open('E:/first_names.txt') as names, open('E:/last_names.txt') as surnames:
    name_list = [line.strip() for line in names.readlines()]
    surname_list = [line.strip() for line in surnames.readlines()]
    #print(name_list)
    #print(surname_list)
    for i in range(3):
        j = random.randint(0,len(name_list))
        k = random.randint(0,len(surname_list))
>>>>>>> ac42a6d0d762e50bbb8e046d51b0be75d6d2195e
        print(name_list[j], surname_list[k])