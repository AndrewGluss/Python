import string
def pig_it(text):
    list_text = text.split(' ')
    #print(list_text)
    for i in range(len(list_text)):
        if list_text[i] not in string.punctuation:
            list_text[i] = list_text[i][1:]+list_text[i][0]+"ay"
    return " ".join(list_text)



def test_pig_it():
    print('testcase #1 - ', end='')
    text = 'Pig latin is cool'
    text_mod = 'igPay atinlay siay oolcay'
    if text_mod == pig_it(text):
        print("OK!")
    else:
        print("Fail")

    print('testcase #2 - ', end='')
    text = 'Hello world !'
    text_mod = 'elloHay orldway !'
    if text_mod == pig_it(text):
        print("OK!")
    else:
        print("Fail")

    print('testcase #3 - ', end='')
    text = 'This is my string'
    text_mod = 'hisTay siay ymay tringsay'
    if text_mod == pig_it(text):
        print("OK!")
    else:
        print("Fail")

if __name__ == "__main__":
    test_pig_it()