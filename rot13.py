# put your python code here
import string
def rot13(message):
    '''
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
    ROT13 is an example of the Caesar cipher.
    Create a function that takes a string and returns the string ciphered with Rot13.
    If there are numbers or special characters included in the string, they should be returned as they are.
    Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
    '''
    listMessage = message.split(' ')
    n = 13
    resultList = []
    for word in listMessage:
        resultWord = ""
        for ind in range(len(word)):
            if word[ind] in string.punctuation or word[ind] in string.digits:
                resultWord += word[ind]
            if ord(word[ind]) in range(97, 123):
                if (ord(word[ind]) + n) > 122:
                    a = n - (122 - ord(word[ind]))
                    resultWord += chr(96 + a)
                else:
                    resultWord += chr(ord(word[ind]) + n)
            if ord(word[ind]) in range(65, 91):
                if (ord(word[ind]) + n) > 90:
                    a = n - (90 - ord(word[ind]))
                    resultWord += chr(64 + a)
                else:
                    resultWord += chr(ord(word[ind]) + n)
            if ord(word[ind]) in range(1072, 1104):
                if (ord(word[ind]) + n) > 1103:
                    a = n - (1103 - ord(word[ind]))
                    resultWord += chr(1071 + a)
                else:
                    resultWord += chr(ord(word[ind]) + n)
            if ord(word[ind]) in range(1040, 1072):
                if (ord(word[ind]) + n) > 1071:
                    a = n - (1071 - ord(word[ind]))
                    resultWord += chr(1039 + a)
                else:
                    resultWord += chr(ord(word[ind]) + n)
        resultList.append(resultWord)
    return " ".join(resultList)
