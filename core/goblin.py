from core.player import General
import random


class Goblin(General):
    weapons = ["knife", "sword", "ax"]

    def __init__(self, name):
        super().__init__(name)
        self.type = "goblin"
        self.hp = 20
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = Goblin.weapons[random.randint(0, 2)]

    def speak(self):
        print(f"the {self.type} {self.name} angry")

    def run_away(self):
        pass

