#Battlefield
from player import Player


class Gameplay:
    def __init__(self):
        self.player_one = ()
        self.player_two = ()

    def start_game(self):
        print ('The game will begin!')
        choices = ["rock", "paper", "scissors", "lizard", "Spock"]
        print(choices)
        
        #if Player() == Player()#will () this assocate picked players?


#Display rules, what beats what?
            # print("Here are the rules of the game: Each player will have an oppotunity to choose a method. /n
            # "Player one will choose a method and then Player two will have a turn. Each player will repeat /n
            # "the steps 2 more times, unless there are any ties. In which case each player will get another go /n
            # "until both players choose something different.")
            # print("What wins?/n"
            #  "Rock crushes Scissors /n"
            #  "Scissors cuts Paper/n"
            #  "Paper covers Rock/n"
            #  "Rock crushes Lizard/n"
            #  "Lizared poisons Spock/n"
            #  "Spock smashes Scissors/n"
            #  "Scissors decapitates Lizard/n"
            #  "Lizard eats Paper /n"
            #  "Paper disaproves Spock/n"
            #  "Spock vaporizes Rock/n")


#Determine game type - single or multi-player
#Create players basone on game type

#Game rounds - Repeat until one player has 2 points
#Player one chooses a gesture
#-Prompt user to enter gesture
#-Save choice somewhere
#Player Two chooses a gesture
#Compare gestures
#--Winner gets a point
# -- No points if tie round
#Display winner of round

#end game
#display winner of game
#Prompt if they want to play again

    def determine_game_type(self):
#set self.player_two to Human or AI