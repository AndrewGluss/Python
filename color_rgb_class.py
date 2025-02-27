class Color:

    def __init__(self, hexcode):
        self._hexcode = hexcode
        self.r = int('0x'+hexcode[:2], 16)
        self.g = int('0x'+hexcode[2:4], 16)
        self.b = int('0x'+hexcode[4:], 16)

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, newhexcode):
        self._hexcode = newhexcode
        self.r = int('0x'+newhexcode[:2], 16)
        self.g = int('0x'+newhexcode[2:4], 16)
        self.b = int('0x'+newhexcode[4:], 16)


color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)


color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)