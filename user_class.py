class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self,n):
        self.friends += n


class User2:

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha() and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Некорректное имя")

    def get_name(self):
        return self._name

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age < 111:
            self._age = age
        else:
            raise ValueError("Некорректный возраст")

    def get_age(self):
        return self._age


user = User('Timur')

user.add_friends(2)
user.add_friends(2)
user.add_friends(3)

print(user.friends)


user2 = User2('Гвидо', 67)

user2.set_name('Тимур')
user2.set_age(30)

print(user2.get_name())
print(user2.get_age())
