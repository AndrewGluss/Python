class OrderedSet:
    def __init__(self, iters=None):
        self.data = [i for i in iters] if iters else []
        self.order_set = self.fill_set()
        self.index = -1

    def __len__(self):
        return len(self.order_set)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key < 0 or key >= len(self.order_set):
            raise IndexError('Неверный индекс')
        return self.order_set[key]

    def __contains__(self, item):
        return item in self.order_set

    def __iter__(self):
        yield from self.order_set

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.order_set == other.order_set
        elif isinstance(other, set):
            return set(self.order_set) == other
        return NotImplemented

    def add(self, value):
        if value not in self.order_set:
            self.order_set.append(value)

    def discard(self, value):
        if value in self.order_set:
            self.order_set.remove(value)

    def fill_set(self):
        result = []
        for item in self.data:
            if item not in result:
                result.append(item)
        return result