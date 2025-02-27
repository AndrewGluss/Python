class TextHandler:

    def __init__(self):
        self.words = []



    def add_words(self, text):
        for i in text.split():
            self.words.append(i)

    def get_shortest_words(self):
        x = [len(i) for i in self.words]
        return [i for i in self.words if len(i) == min(x)]

    def get_longest_words(self):
        x = [len(i) for i in self.words]
        return [i for i in self.words if len(i) == max(x)]

texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())


texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())


texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
