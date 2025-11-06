import random


class General:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def attack(self, dice):
        return self.speed + dice


class Player(General):
    professional = ["cure", "fighter"]

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.hp = 50
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)

        self.armor_rating = random.randint(5, 15)
        self.profession = Player.professional[random.randint(0, 1)]

    def speak(self):
        print(f"this is {self.name} talk")

    def rise_power(self):
        self.power += 2

    def rise_hp(self):
        self.hp += 10
