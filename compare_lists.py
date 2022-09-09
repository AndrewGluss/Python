def compare_lists(list1, list2):
    """Функция принимает на вход два списка, и возвращает список из элементов первого списка,
    которые есть в элементах второго списка, иначе пустой список
    """
    compare = []
    for i in list1:
        for j in list2:
            if i in j and i not in compare:
                compare.append(i)
    return compare

def test_compare():
    print("testcase #1: - ", end='')
    list1 = ["arp", "live", "strong"]
    list2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    result = ["arp", "live", "strong"]
    if result == compare_lists(list1, list2):
        print("OK!")
    else:
        print("Failed!")

    print("testcase #2: - ", end='')
    list1 = ["tarp", "mice", "bull"]
    list2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    result = []
    if result == compare_lists(list1, list2):
        print("OK!")
    else:
        print("Failed!")

if __name__ == "__main__":
    test_compare()