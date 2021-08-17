#from random import Random
import random
from player import Player

class AIplayer(Player):
    def __init__(self):
        self.player_name = 'Computer'
        super().__init__()
        
    def choose_option(self):
        self.choice = random.randint(1,5) 
        #choose = self.gesture_list[choice]
        #print("Result: " + str(self.choice))
        if self.choice == 1:
            print("Computer choice: Rock")
        if self.choice == 2:
            print("Computer choice: Scissors")
        if self.choice == 3:
            print("Computer choice: Paper")
        if self.choice == 4:
            print("Computer choice: Lizard")
        if self.choice == 5:
            print("Computer choice: Spock")
       