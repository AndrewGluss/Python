from copy import deepcopy


class PermaDict:

    def __init__(self, dict_obj: dict | None = None):
        self.dict = deepcopy(dict_obj) if dict_obj else {}

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        if key not in self.dict:
            self.dict[key] = value
        else:
            raise KeyError("Изменение значения по ключу невозможно")

    def __delitem__(self, key, ):
        del self.dict[key]

    def __len__(self):
        return len(self.dict.keys())

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

    def __iter__(self):
        yield from self.dict.keys()




permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)