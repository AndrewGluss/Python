def gematria(word):
    summ = 0
    for i in word:
        summ += ord(i.upper())-ord('A')
    return summ
words = []
n = int(input())
for i in range(n):
    words.append(input())
new_words = sorted(words)
print(*sorted(new_words, key = gematria), sep = '\n')

