class ReadableTextFile:

    def __init__(self, path):
        self.path = path
        self.file = None
        self.content = []


    def __enter__(self):
        self.file = open(self.path, mode='r', encoding='utf-8')
        for line in self.file:
            self.content.append(line.strip())

        return self.content

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with open('poem.txt', 'w', encoding='utf-8') as file:
    print('Я кашлянул в звенящей тишине,', file=file)
    print('И от шального эха стало жутко…', file=file)
    print('Расскажет ли утятам обо мне', file=file)
    print('под утро мной испуганная утка?', file=file)

with ReadableTextFile('poem.txt') as file:
    for line in file:
        print(line)