class WritableTextFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, mode='w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


with WritableTextFile('output.txt') as file:
    file.write('Python generation!')