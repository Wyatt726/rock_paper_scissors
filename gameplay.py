#Battlefield
class Gameplay:
    def __init__(self):
        self.player_one = ()
        self.player_two = ()

    def start_game(self):
        # print("The game will begin!")
        # choices = ["rock", "paper", "scissors", "lizard", "Spock"]
        # computer = random.choice(choices)
#Welcome message
print("Welcome to RPSLS!")
#Display rules, what beats what?
print("Here are the rules of the game: Each player will have an oppotunity to choose a method.")
print("Player one will choose a method and then Player two will have a turn.")
print("Each player will repeat the steps 2 more times, unless there are any ties.")
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