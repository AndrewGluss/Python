n = int(input())
phoneDict = {}
for i in range(n):
  print(i)
  stroka = input()
  list1 = stroka.split()
  print(list1)
  name = list1[-1].lower()
  phone = list1[0]
  if name not in phoneDict:
    phoneDict[name] == phone
  else:
    phoneDict.setdefault(name, []).append(phone)
m = int(input())
for i in range(m):
  s = input().lower()
  print(phoneDict.get(s, "абонент не найден"))