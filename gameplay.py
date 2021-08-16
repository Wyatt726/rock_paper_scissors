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

        if(self.game_mode == "1"):
            self.player_one = Human()
            self.player_two = AIplayer()
        elif(self.game_mode == "2"):
            self.player_one = Human()
            self.player_two = Human()
        elif(self.game_mode == "3"):
            self.player_one = AIplayer()
            self.player_two = AIplayer()
        
       
       # self.player_one.assign_name("1")
       # self.player_two.assign_name("2")      
         
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
        if self.player_one.choice == "rock" and self.player_two.choice == "rock":
           print("It's a tie!") 
        if self.player_one.choice == "rock" and self.player_two.choice == "scissors":
            print("Rock crushes scissors, Player_one wins!")
            self.player_one.score += 1
        if choice == ""
        pass


    #player score less than 2 keep looping -- while loop