'''Генерация карточки для игры бинго'''
import random
bingo1 = [i for i in range(1,76)]
bingo = random.sample(bingo1, 25)
bingo[12] = 0
#print(bingo)
for i in range(5):
  stroka = bingo[0:5]
  for i in stroka:
    print(str(i).ljust(3,' '),end = ' ')
  bingo = bingo[5:]
  print()