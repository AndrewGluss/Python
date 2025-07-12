def linear_coefficients(p1, p2):
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = (p1[1] * p2[0] - p1[0] * p2[1]) / (p2[0] - p1[0])

    return (k, b)