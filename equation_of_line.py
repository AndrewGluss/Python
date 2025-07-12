def equation_of_line(values):
    list_x = [0, 1, 2, 3, 4]
    y2 = values[-1]
    y1 = values[0]
    x1 = list_x[0]
    x2 = list_x[-1]
    k = int((y2 - y1 ) / (x2 - x1))
    b = int((y1 * x2 - x1 * y2) / (x2 - x1))
    flag = False
    for i, j in zip(list_x, values):
        if j == k * i + b:
            flag = True
        else:
            flag = False
            break


    if flag:
        if k >=2 or k <=-2:
            if b >= 1:
                return f"y = {k}x + {b}"
            if b <= -1:
                return f"y = {k}x - {abs(b)}"
            if b == 0:
                return f"y = {k}x"
        if k == 1:
            if b >= 1:
                return f"y = x + {b}"
            if b <= -1:
                return f"y = x - {abs(b)}"
            if b == 0:
                return f"y = x"
        if k == -1:
            if b >= 1:
                return f"y = -x + {b}"
            if b <= -1:
                return f"y = -x - {abs(b)}"
            if b == 0:
                return f"y = -x"
        if k == 0:
            if b != 0:
                return f"y = {b}"
            if b == 0:
                return f"y = 0"
    return None

print(equation_of_line([0, 1, 2, 3, 4]))
print(equation_of_line([0, -1, -2, -3, -4]))
print(equation_of_line([0, -2, -4, -6, -8]))
print(equation_of_line([1, 3, 5, 7, 9]))
print(equation_of_line([6, 6, 6, 6, 6]))
print(equation_of_line([1, 1, 2, 2, 2]))
