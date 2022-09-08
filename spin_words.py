def spinWords(text):
    """Функция принимает на вход строку, состоящую только из букв и пробелов
    и возвращает строку, в которой слова перевернуты, если  длина слова больше или равна 5
    """
    text_list = [i for i in text.split(" ")]
    for i in range(len(text_list)):
        if len(text_list[i]) >= 5:
            text_list[i] = text_list[i][::-1]
    spin_text = ' '.join(text_list)
    return spin_text


def test_spin():
    print('testcase #1 - ', end='')
    text = 'Hey fellow warriors'
    text_mod = 'Hey wollef sroirraw'
    if text_mod == spinWords(text):
        print("OK!")
    else:
        print("Fail")

    print('testcase #2 - ', end='')
    text = 'This is a test'
    text_mod = 'This is a test'
    if text_mod == spinWords(text):
        print("OK!")
    else:
        print("Fail")

    print('testcase #3 - ', end='')
    text = 'This is another test'
    text_mod = 'This is rehtona test'
    if text_mod == spinWords(text):
        print("OK!")
    else:
        print("Fail")

if __name__ == "__main__":
    test_spin()