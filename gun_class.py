class Gun:
    def __init__(self):
        pass

    def shoot(self):
        print('pif')


class Gun2:
    def __init__(self):
        self.count = 0

    def shoot(self):
        if self.count % 2 == 0:
            print('pif')
            self.count += 1
        else:
            print('paf')
            self.count += 1

class Gun3:
    def __init__(self):
        self.count = 0

    def shoot(self):
        if self.count % 2 == 0:
            print('pif')
            self.count += 1
        else:
            print('paf')
            self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()


gun2 = Gun2()

gun2.shoot()
gun2.shoot()
gun2.shoot()
gun2.shoot()


gun3 = Gun3()

gun3.shoot()
gun3.shoot()
print(gun3.shots_count())
gun3.shots_reset()
print(gun3.shots_count())
gun3.shoot()
print(gun3.shots_count())