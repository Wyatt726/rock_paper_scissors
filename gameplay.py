#Battlefield
from player import Player

class Gameplay:
    def __init__(self):
        self.player_one = ()
        self.player_two = ()

    def start_game(self):
        print ('The game will begin!')
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        print(choices)

    def display_welcome(self):
            print("Welcome to the Rock, Paper, Scissors...Lizard and Spock game! - The only one of its kind!")    

    def game_rules(self):
            print("Here are the rules of the game: /n"
            "1. Player one selects a gesture./n"
            "2. Player two selects a gesture./n"
            "3. As long as there is not a tie, repeat sequence two more times./n"
            " Best of three wins.")

    def criteria(self):
            print("What wins?/n"
             "Rock crushes Scissors /n"
             "Scissors cut Paper/n"
             "Paper covers Rock/n"
             "Rock crushes Lizard /n"
             "Lizard poisons Spock/n"
             "Spock smashes Scissors/n"
             "Scissors decapitates Lizard/n"
             "Lizard eats Paper /n"
             "Paper disapproves Spock/n"
             "Spock vaporizes Rock/n")

#Determine game type - single or multi-player
    def determine_game_mode(self):
        #gain user input
        self.game_mode = input("How would you like to play? Enter 1 for single player or 2 for multiplayer below.")
        if "user_input" == 1: 
            print("You vs. Computer")
        if "user_input" == 2:
            print("You vs. Player Two")
        #set self.player_two to Human or AI
        
#Create players based on game type

#Game rounds - Repeat until one player has 2 points - while loop?
    def gesture_battle(self):
        pass
#-Prompt user to enter gesture
    def player_one_turn(self):
        self.player_one_turn = input("Enter the appropriate number for your choice: /n"
             "1 - Rock /n"
             "2 - Scissors /n"
             "3 - Paper /n"
             "4 - Lizard /n"
             "5 - Spock/n")
#if Player() == Player()#will () this assocate picked players?
#-Save choice somewhere
        print("Player One " + input)
#Player Two chooses a gesture
    def player_two_turn(self):
        self.player_two_turn = input("Enter the appropriate number for your choice: /n"
             "1 - Rock /n"
             "2 - Scissors /n"
             "3 - Paper /n"
             "4 - Lizard /n"
             "5 - Spock/n")
        print("Player Two " + input)
#Compare gestures
    def compare_gestures(self):
        pass
#--Winner gets a point
    def count_points(self):
        pass 
# -- No points if tie round
#Display winner of round
    def round_winner(self):
        pass
#end game
#display winner of game
    def display_winner(self):
        if "Player One" == 3:
            print("Player One, you are the winner!")
        else:
            print("Congratulations Player Two!")

#Prompt if they want to play again
    def play_again(self):
        self.players = input("Would you like to play again? Enter 'yes' or 'no' below.")

        