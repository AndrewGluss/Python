from copy import deepcopy


class CyclicList:
    def __init__(self, data=[]):
        self.data = deepcopy(data)
        self.index = -1

    def __len__(self):
        return len(self.data)

    def append(self, value):
        self.data.append(value)

    def pop(self, key=-1):
        x = self.data.pop(key)
        return x

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index >= len(self.data):
            self.index = 0

        return self.data[self.index]

    def __getitem__(self, key):
        if key >= len(self.data):
            return self.data[key % len(self.data)]
        else:
            return self.data[key]



cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))