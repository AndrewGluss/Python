class Pet:
    names = []
    nums = 0

    def __init__(self, name):
        Pet.names.append(self)
        Pet.nums += 1
        self.name = name

    def first_pet():
        if len(Pet.names) > 0:
            return Pet.names[0]
        else:
            return None

    def last_pet():
        if len(Pet.names) > 0:
            return Pet.names[-1]
        else:
            return None

    def num_of_pets():
        return Pet.nums


print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())



pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())