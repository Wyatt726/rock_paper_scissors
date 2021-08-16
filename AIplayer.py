from random import Random
from player import Player

class AIplayer(Player):
    def __init__(self):
        self.player_name = 'Arti'
        super().__init__()

    def choose_option(self):
        self.choice = Random.choice(self.gesture_list)
        print(AIplayer)
        

      