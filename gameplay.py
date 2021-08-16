#Gamefield
from humanplayer import Humanplayer
from player import Player
from AIplayer import AIplayer
from collections import Counter

class Gameplay:
    def __init__(self):
        self.player_one = Humanplayer()
        self.player_two = Player()
        self.player_ai = AIplayer

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
            "Winner receives 1 point per turn - Best of three wins.")

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
             "Paper disproves Spock/n"
             "Spock vaporizes Rock/n")

#Determine game type - single or multi-player / gain user input
#resouce: https://codeabcs.com/python/validation.php
    def determine_game_mode(self):
        self.game_mode = input("How would you like to play?")
        while True:
            try:
                0 = int(input("Please enter 1 for single player or 2 for multiplayer."))
                if 0 >= 3:
                    raise ValueError("This is not a correct option. Please re-enter.")
            except ValueError as error:
                print("That is not a valid option. Please enter 1 or 2.")
            else:
                print("Thank you.")
                break                               
  
# enter names
        self.player_one.assign_name("1")
        self.player_two.assign_name("2")
        #set self.player_two to Human or AI
        
#Create players based on game type

#Game rounds - Repeat until one player has 2 points - while loop?
    def gesture_battle(self):
        self.p1 = input("Enter the appropriate number for your choice: /n"
             "1 - Rock /n"
             "2 - Scissors /n"
             "3 - Paper /n"
             "4 - Lizard /n"
             "5 - Spock/n")
        print("Player One: " + input)

#if Player() == Player()#will () this assocate picked players?

#-Save choice somewhere

#Player Two chooses a gesture
    def p2(self):
        self.p2 = input("Enter the appropriate number for your choice: /n"
             "1 - Rock /n"
             "2 - Scissors /n"
             "3 - Paper /n"
             "4 - Lizard /n"
             "5 - Spock/n")
        print("Player Two: " + input)

#Compare gestures
    player_one = "p1"
    player_two = "p2"

    def compare_gestures(self):
        if ("p1" == 1 < 2 or "p2" == 1 < 4):
            print("Rock Wins!")
        if ("p1" == 2 < 3 or "p2" == 2 < 4):
            print("Scissors Wins!")
        if ("p1" == 3 > 1 or "p2" == 3 < 5):
            print("Paper Wins!")
        if ("p1" == 4 < 5 or "p2" == 5 > 3):
            print("Lizard Wins!")
        if ("p1" == 5 > 2 or "p2" == 5 > 1):
            print("Spock Wins!")
        if ("p1" == "p2"):
            print("Tie")
      
#--Winner gets a point               Not sure how to do this??????????
    def count_points(self):
        print(Counter(["Player One: ", "Player Two: "]))

#Display winner of round
    def round_winner(self):
        player_one_points = 0
        if player_one_points >= 1:
            print("Player one, you are the winner of this round!")
        else:
            print("Player Two, you are the winner of this round!")

#end game
#display winner of game
    def display_winner(self):
        if ("Player One" == 2):
            print("Player One, you are the winner of this game!")
        else:
            print("Congratulations Player Two! You are the winner!")

#Prompt if they want to play again
    def play_again(self):
        self.players = input("Would you like to play again? Enter 'yes' or 'no' below.")
        if input == "yes":
            pass                 #how to start game over????
        elif input == "no":
            print("Thank you for playing!")
        else:
            print ("")         