def on_one_line(p1, p2, p3):
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = (p1[1] * p2[0] - p1[0] * p2[1]) / (p2[0] - p1[0])

    if p3[1] == k * p3[0] + b:
        return True
    return False