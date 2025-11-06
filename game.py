import random

from core.orc import Orc
from core.goblin import Goblin
from core.player import General
from core.player import Player


class Game:
    def start(self):
        return ("""
--------menu-------
1.fight
2.exit
        """)

    def show_menu(self):
        print(self.start())
        choose = input("please enter 1 for fight or 2 for exit")
        return choose

    def choose_random_monster(self):
        monster1 = Orc("orc")
        monster2 = Goblin("goblin")
        monster_list = [monster1, monster2]
        random_monster = random.randint(0, 1)
        return monster_list[random_monster]

    @staticmethod
    def roll_dice(side: int):
        dice = random.randint(1, side)
        return dice

    @staticmethod
    def battle(player, monster, dice1, dice2, choose):
        if choose == "2":
            exit()
        else:
            if player.profession == "cure":
                player.rise_hp()
            else:
                player.rise_power()
            player_attack = player.attack(dice1)
            monster_attack = monster.attack(dice1)
            print(player_attack)
            print(monster_attack)
            while player.hp != 0 and monster.hp != 0:
                if monster_attack > player_attack:
                    attack = monster
                    attacked = player
                    check = monster.attack(dice2)
                    if check > player.armor_rating:
                        if monster.weapon == "knife":
                            damage = monster.power * 0.5
                            player.hp -= damage

                        elif monster.weapon == "sword":
                            player.hp -= monster.power

                        else:
                            damage = monster.power * 1.5
                            player.hp -= damage
                        print(f"{monster.name} injury hp = {monster.hp}")
                    else:
                        print("miss your turn")
                        attacked, attack = attack, attacked
                elif player_attack > monster_attack:
                    attack = player
                    attacked = monster
                    check = attack.attack(dice2)
                    if check > monster.armor_rating:

                        monster.hp -= attack
                        print(f"{monster.name} injury hp = {monster.hp}")

                    else:
                        print("miss your turn")
                        attacked, attack = attack, attacked
