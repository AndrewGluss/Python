from copy import deepcopy

class HistoryDict:

    def __init__(self, data: dict | None = None):
        self.data = deepcopy(data) if data else {}
        self._history = {key: [value] for key, value in self.data.items()}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        if key not in self.data:
            self.data[key] = value
            self._history[key] = [value]
        else:
            self._history[key].append(value)
            self.data[key] = value

    def __delitem__(self, key,):
        del self.data[key]
        del self._history[key]

    def __len__(self):
        return len(self.data.keys())

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history

    def __iter__(self):
        yield from self.data.keys()


historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())