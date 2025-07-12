class SparseArray:
    def __init__(self, default):
        self.default = default
        self.sparsearray = {}

    def __setitem__(self, key, value):
        if key not in self.sparsearray.keys():
            self.sparsearray[key] = value

    def __getitem__(self, key):
        if key not in self.sparsearray.keys():
            return self.default
        else:
            return self.sparsearray[key]


array = SparseArray(None)

array[0] = 'Timur'
array[1] = 'Arthur'

print(array[0])
print(array[1])
print(array[2])