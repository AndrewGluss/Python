from re import sub, IGNORECASE

def normalize_whitespace(text):
    newtext = sub(r'( ){2,}', r' ', text)

    return newtext

print(normalize_whitespace('AAAA                A                AAAA'))
print(normalize_whitespace('Тут нет лишних пробелов'))
print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
# TEST_4:
print(normalize_whitespace('K L  L    O    I!  !  I OP    PPPppdj O   P'))

# TEST_5:
print(normalize_whitespace('               '))

# TEST_6:
print(normalize_whitespace('aaaaaaaaaaaaaaaaaaaaaaaaaa'))

# TEST_7:
print(normalize_whitespace('Раз два  три   четыре    пять      шесть      '))

# TEST_8:
print(normalize_whitespace('      Шесть-----пять    четыре***три  два+один'))

# TEST_9:
print(normalize_whitespace('1 9  2  8   3   7    6    5'))

# TEST_10:
print(normalize_whitespace('Проб.елов,нетв-этом:очень\длинно*мслове'))

# TEST_11:
print(normalize_whitespace(''))

# TEST_12:
print(normalize_whitespace(' '))

# TEST_13:
print(normalize_whitespace('There are no unnecessary gaps.'))

# TEST_14:
print(normalize_whitespace('. ,  ;   :    "     (       )      '))

# TEST_15:
print(normalize_whitespace('111111111111 2222222222222 333333333333'))