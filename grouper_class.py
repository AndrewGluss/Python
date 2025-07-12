class Grouper:

    def __init__(self, iter_obj, key):
        self.iter_obj = iter_obj
        self.key = key
        self.group = {}

        for item in iter_obj:
            if self.key(item) in self.group:
                self.group[self.key(item)].append(item)
            else:
                self.group[self.key(item)] = [item]

    def __getitem__(self, key):
        return self.group[key]

    def __contains__(self, item):
        return item in self.group

    def add(self, item):
        if self.key(item) in self.group:
            self.group[self.key(item)].append(item)
        else:
            self.group[self.key(item)] = [item]

    def group_for(self, item):
        return self.key(item)

    def __len__(self):
        return len(self.group.keys())

    def __iter__(self):
        yield from self.group.items()


grouper = Grouper(['hi'], key=lambda s: s[0])
print(len(grouper))

grouper.add('hello')
grouper.add('bee')
grouper.add('big')

print(len(grouper))

grouper.add('geek')
print(grouper['h'])
print(grouper['b'])
print(grouper['g'])

print(len(grouper))



grouper = Grouper(['hi'], key=lambda s: s[0])

print(grouper.group_for('hello'))
print(grouper.group_for('bee'))
print(grouper['h'])
print('b' in grouper)