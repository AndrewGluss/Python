class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[~key]


numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])