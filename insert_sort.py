def insert_sort(A):
    """ Сортировка вставками списка А
    """
    n = len(A)
    # top - верхушка массива
    for top in range(1, n):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def test_sort(sort_algorithm):
    print("Тестируем: ", insert_sort.__doc__)
    print("testcase #1: ", end=''
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
    test_sort(insert_sort)