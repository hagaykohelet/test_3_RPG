import random
from core.player import General


class Orc(General):
    weapons = ["knife", "sword", "ax"]

    def __init__(self, name):
        super().__init__(name)
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = Orc.weapons[random.randint(0, 2)]

    def speak(self):
        print(f"the {self.type} {self.name} angry")

