class SequenceZip:
    def __init__(self, *args):
        self.args = list(zip(*args))
        self.index = -1

    def __len__(self):
        return len(self.args)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key < 0 or key >= len(self.args):
            raise IndexError('Неверный индекс')
        return self.args[key]

    def __contains__(self, item):
        return item in self.args

    def __iter__(self):
        yield from self.args


data1 = [1, 2, 3, 4, 5]
data2 = 'abcde'

sequencezip = SequenceZip(data1, data2)
data1.extend([6, 7, 8, 9, 10])
data2 += 'fghij'

print(data1)
print(data2)
print(len(sequencezip))
print(list(sequencezip))
