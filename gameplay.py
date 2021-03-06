#Gamefield
from player import Player
from human import Human

#from player import Player
from AIplayer import AIplayer

#-------------------constructor-----------------
class Gameplay:
    def __init__(self):
        #self.player = Player
        self.player_one = None
        self.player_two = None
      
        

#---------------method signatures---------------
    def run_game(self):
        self.game_details()
        self.determine_game_mode()
        self.game_rounds()
        self.compare_choices()
        
    def game_details(self):
        self.welcome = print("Welcome to the Rock, Paper, Scissors...Lizard and Spock game!")

        self.rules = print("Here are the rules of the game: 1. Player one selects a gesture. 2. Player two selects a gesture. 3. As long as there is not a tie, repeat sequence two more times. The winner receives 1 point per turn - Best of three wins.")

        self.criteria = print("What wins? Rock crushes Scissors, Scissors cut Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,   Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")
    
    def determine_game_mode(self):
        self.game_mode = input("Would you like to play single player or multiplayer? Enter 1 for single or 2 to play a friend. ")

        if(self.game_mode == "1"):
            self.player_one = Human()
            self.user_input = input("Player one, please enter your name below: ")
            print("Hi " + self.user_input)
            self.player_two = AIplayer()
            print("You vs. Computer")
        elif(self.game_mode == "2"):
            self.player_one = Human()
            self.user_input = input("Player one, please enter your name below: ")
            print("Hi " + self.user_input)
            self.player_two = Human()
            self.user_input = input("Player two, please enter your name below: ")
            print("Hi " + self.user_input)

    def game_rounds(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_option()
            self.player_two.choose_option()
            self.compare_choices()
           
        if self.player_one.score > 2:
            print ("player one wins!")
        elif self.player_two.score > 2:
                print("player two wins!")
    
    def compare_choices(self):
            if self.player_one == "1" and self.player_two == "2":
                print("Rock crushes scissors, Player_one wins!")
                self.player_one.score += 1
            elif self.player_one.choice == "scissors" and self.player_two.choice == "paper":
                print("Scissors cuts paper! Player_one wins!")
                self.player_one.score += 1
            elif self.player_one.choice == "paper" and self.player_two.choice == "rock":
                print("Paper covers rock! Player_one wins!")
                self.player_one.score += 1
            elif self.player_one.choice == "lizard" and self.player_two.choice == "Spock":
                print("lizard poisons Spock! Player_one wins!")
                self.player_one.score += 1
            elif self.player_one.choice == "Spock" and self.player_two.choice == "scissors":
                print("Spock smashes scissors! Player_one wins!")
                self.player_one.score += 1
            elif self.player_two.choice == "rock" and self.player_one.choice == "lizard":
                print("rock crushes lizard! Player_two wins!")
                self.player_two.score += 1
            elif self.player_two.choice == "scissors" and self.player_one.choice == "lizard":
                print("Scissors decapitates lizard! Player_two wins!")
                self.player_two.score += 1
            elif self.player_two.choice == "paper" and self.player_one.choice == "Spock":
                print("paper disproves Spock! Player_two wins!")
                self.player_two.score += 1
            elif self.player_two.choice == "lizard" and self.player_one.choice == "paper":
                print("Lizard eats paper! Player_two wins!")
                self.player_two.score +=1
            elif self.player_two.choice == "Spock" and self.player_one.choice == "scissors":
                print("Spock smashes scissors! Player_two wins!")
                self.player_two.score +=1                  
        # else:
        #     print("You both chose the same thing!")  