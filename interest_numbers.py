def all_numb(numb):
    count = 0
    for i in str(numb):
        if numb%int(i)==0:
            count +=1
    if count == len(str(numb)):
        return True

a, b = int(input()), int(input())
numbers = [i for i in range(a,b+1)]
interest_numbers = []
for i in numbers:
    x = [int(k) for k in str(i)]
    if all(x):
        if all_numb(i):
            interest_numbers.append(i)
print(*interest_numbers)