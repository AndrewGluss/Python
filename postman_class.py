class Postman:

    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        if tuple([street, house, flat]) not in self.delivery_data:
            self.delivery_data.append(tuple([street, house, flat]))

    def get_houses_for_street(self, street):
        x = [i[1] for i in self.delivery_data if i[0] == street]
        houses = []
        for i in x:
            if i not in houses:
                houses.append(i)
        return houses

    def get_flats_for_house(self, street, house):
        return [i[2] for i in self.delivery_data if i[0] == street and i[1] == house]


postman = Postman()

print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))

