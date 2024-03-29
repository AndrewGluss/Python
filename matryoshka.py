def matryoshka(n):
    """Рекурсия на примере матрёшки
    """
    # Определяем базовый/крайний случай
    if n == 1:
        print("Матрешка")
    # Определяем рекурентый случай, когда функция вызывает саму себя
    else:
        print("Верх матрешки", n)
        matryoshka(n-1)
        print("Низ матрешки", n)

if __name__ == "__main__":
    matryoshka(5)