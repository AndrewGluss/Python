class Wordplay:

    def __init__(self, words=[]):
        self.words = [*words]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [i for i in self.words if len(i) == n]

    def only(self, *args):
        return [i for i in self.words if set(i).issubset(args)]

    def avoid(self, *args):
        return [i for i in self.words if set(i).isdisjoint(set(args))]


wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only('a', 'b', 'c'))
print(wordplay.avoid('a', 'b', 'c'))

wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)

wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])

wordplay.add_word('python')
print(wordplay.words_with_length(4))


wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))