def spec_return_list(n,X, Y,A,B):
    '''Функция принимает на вход параметры n, X, Y, A, B, где n - количество элементов в списке > 0
    X, Y, A, B - элементы списка, X<Y,A<B,  1≤X,Y,A,B≤ n
    На выходе получается список в котором часть элементов от элемента с номером X до элемента с номером Y,
    а затем от элемента с номером A до элемента с номером B расположены в обратно порядке
    spec_return_list(9,2,5,6,9) -> [1, 2, 6, 5, 8, 7, 3, 4, 9]
    spec_return_list(9,3,6,5,8) -> [1, 5, 4, 3, 2, 9, 8, 7, 6]
    '''
    numbers = [i for i in range(n+1)]
    firstRotate = numbers[:X] + numbers[Y:X-1:-1] + numbers[Y+1:]
    secondRotate = firstRotate[:A] + firstRotate[B:A-1:-1] + firstRotate[B+1:]
    return secondRotate[1:]
    # ' '.join([str(i) for i in secondRotate[1:]])

print(spec_return_list(9,2,5,6,9))