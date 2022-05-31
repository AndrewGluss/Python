pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for tuples in pets:# для каждого кортежа в списке
    elem = list(tuples)# переводим кортеж в список ['Hatiko', 'Parker', 'Wilson', 50]
    key = tuple(elem[1:])# переводим в кортеж данные о владельце собаки, будет ключ словаря ('Parker', 'Wilson', 50)
    value = elem[0]# кличка собаки будет значением словаря 'Hatiko'
    if key not in result:
        list1 = []
        list1.append(value)
        result[key] = list1
    else:
        list1 = result[key]
        list1.append(value)
        result[key] = list1
for key, value in result.items():
    print(key, ':', value)