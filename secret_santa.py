'''Генерируем список участников для тайного санты'''
import random
n = int(input())# количество участников
participants = []
for i in range(n):
  participants.append(input())# заполняем список участниками
santa = participants.copy()# копируем список
random.shuffle(participants)# перемешиваем исходный список
secret_santa = dict()# создаем словарь
count = 0
while count != n:# до тех пор пока если совпадения в списках по индексу, перемешиваем
  for i in range(n):
    if santa[i] == participants[i]:
      count = 0
    else:
      count += 1
  if count != n:
    random.shuffle(participants)
for i in range(n):
  secret_santa[santa[i]] = participants[i]
for key, value in secret_santa.items():
    print(key, '-', value)