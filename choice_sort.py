def choice_sort(A):
    """ Сортировка выбором списка А
    """
    n = len(A)
    # pos - позиция элементов
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if A[k] < A[pos]:
                A[pos], A[k] = A[k], A[pos]

def test_sort(sort_algorithm):
    print("Тестируем: ", choice_sort.__doc__)
    print("testcase #1: ", end='')
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort_algorithm(A)
    print("OK" if A_sorted == A else "Failed")

    print("testcase #2: ", end='')
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(0,20))
    sort_algorithm(A)
    print("OK" if A_sorted == A else "Failed")

    print("testcase #3: ", end='')
    A = [4, 2, 4, 1, 2]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("OK" if A_sorted == A else "Failed")

if __name__ == "__main__":
    test_sort(choice_sort)