#Gamefield
from humanplayer import Humanplayer #debugger picks up errors here
from player import Player
from AIplayer import AIplayer
from collections import Counter

#----------constructor-----------------
class Gameplay:
    def __init__(self):
        self.player_one = Player
        self.player_two = Humanplayer
        self.player_ai = AIplayer
        

#---------------method signatures---------------
    def game_details(self):
        self.welcome = print("Welcome to the Rock, Paper, Scissors...Lizard and Spock game!")

        self.rules = print("Here are the rules of the game: /n"
        "1. Player one selects a gesture./n"
        "2. Player two selects a gesture./n"
        "3. As long as there is not a tie, repeat sequence two more times./n"
        "Winner receives 1 point per turn - Best of three wins./n")

        self.criteria = ("What wins?/n"
        "Rock crushes Scissors /n"
        "Scissors cut Paper/n"
        "Paper covers Rock/n"
        "Rock crushes Lizard /n"
        "Lizard poisons Spock/n"
        "Spock smashes Scissors/n"
        "Scissors decapitates Lizard/n"
        "Lizard eats Paper /n"
        "Paper disproves Spock/n"
        "Spock vaporizes Rock/n")
    
    def determine_game_mode(self):
        self.game_mode = input("Would you like to play single player to multiplayer? Enter 1 for single or 2 to play a friend.")
       # self.player_one.assign_name("1")
       # self.player_two.assign_name("2")      
         
    def game_rounds(self):
        self.plyaer_one = input("Enter the appropriate number for your choice: /n"
             "1 - Rock /n"
             "2 - Scissors /n"
             "3 - Paper /n"
             "4 - Lizard /n"
             "5 - Spock/n")
        print("Player One: " + input)

        self.player_two = input("Enter the appropriate number for your choice: /n"
             "1 - Rock /n"
             "2 - Scissors /n"
             "3 - Paper /n"
             "4 - Lizard /n"
             "5 - Spock/n")
        print("Player Two: " + input)

        self.player_ai = ()
        print("Computer: " + input)

    def compare_choices(self):
        choice = ""
        choice2 = ""
        if choice == "rock" and choice2 == "rock":
           print("It's a tie!") 
        if choice == "rock" and choice2 == "scissors":
            print("Rock crushes scissors, Player_one wins!")






