import random
lucky = []
count = 0
num = random.randint(1,49)
while count < 7 and num not in lucky:
    print(num)
    lucky.append(num)
    num = random.randint(1,49)
    count += 1
lucky.sort()
print(*lucky)