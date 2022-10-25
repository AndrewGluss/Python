import random
import string

def generate_index():
    list1 = [i for i in string.ascii_uppercase]
    letter1 = ''.join(random.sample(list1, 2))
    letter2 = ''.join(random.sample(list1, 2))
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)
    index = letter1 + str(num1) + "_" + str(num2) + letter2
    print(index)
generate_index()