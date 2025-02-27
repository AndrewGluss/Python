class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, n):
        self.rooms += n


house = House('white', 4)

house.paint('black')
house.add_rooms(1)

print(house.color)
print(house.rooms)
