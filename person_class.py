class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_fullname(self):
        return self.name + " " + self.surname

    def set_fullname(self, fullname):
        x = fullname.split()
        self.name = x[0]
        self.surname = x[1]

    fullname = property(get_fullname, set_fullname)


class Person2:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()
person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)


person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)


person = Person('Алан', 'Тьюринг')

person.surname = 'Вирт'
print(person.fullname)


person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)



person2 = Person2('Mike', 'Pondsmith')

print(person2.name)
print(person2.surname)
print(person2.fullname)


person2 = Person2('Mike', 'Pondsmith')

person2.fullname = 'Troy Baker'
print(person2.name)
print(person2.surname)