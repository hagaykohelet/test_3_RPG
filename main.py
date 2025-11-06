from core.orc import Orc
from core.goblin import Goblin
from core.player import General
from core.player import Player
from game import Game
player = Player("hagay")
game = Game()
monster = game.choose_random_monster()
game.show_menu()
game.battle(player,monster,game.show_menu(),game.roll_dice(6),game.roll_dice(20))