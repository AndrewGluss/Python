from datetime import date


def is_correct(day1, month1, year1):
    try:
        if date(year1, month1, day1):
            return True
    except:
        return False

count = 0
flag = True
while flag:
    input_date = input()
    if input_date == "end":
        flag = False
        break
    else:
        day, month, year = input_date.split('.')
        if is_correct(int(day), int(month), int(year)):
            print("Корректная")
            count += 1
        else:
            print("Некорректная")
print(count)
