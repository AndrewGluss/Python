'''
На вход программе подается одно слово, записанное в первой строке, затем натуральное число n — количество слов для сравнения и n строк со словами.
Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.
'''
general_word = input()
general_word_ind = [i for i in range(len(general_word)) if general_word[i].lower() in "ауоыиэяюёе"]
n = int(input())
words = []
for i in range(n):
    words.append(input())
for word in words:
    ind = []
    for i in range(len(word)):
        if word[i].lower() in "ауоыиэяюёе":
            ind.append(i)
    if ind == general_word_ind:
        print(word)

