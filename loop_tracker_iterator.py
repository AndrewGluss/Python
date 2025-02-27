class LoopTracker:
    def __init__(self, data):
        self.data = list(data)
        self.index = -1
        self._accesses = 0
        self._empty_accesses = 0
        self._first = self.data[0] if len(data) > 0 else None
        self._last = None
        self._flag = False

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first is None:
            raise AttributeError("Исходный итерируемый объект пуст")
        else:
            return self._first

    @property
    def last(self):
        if self._last is None:
            raise AttributeError("Последнего элемента нет")
        else:
            return self._last

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(list(self.data)) -1:
            self._flag = True
        if self.index >= len(list(self.data)):
            self._empty_accesses += 1
            raise StopIteration
        else:
            self._last = self.data[self.index]
        self._accesses += 1
        return self.data[self.index]


    def is_empty(self):
        return self._flag
