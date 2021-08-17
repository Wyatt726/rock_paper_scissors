from player import Player
class Human(Player):
    def __init__(self):
        self.player_name = ""
        self.player_name = ""
        super().__init__()

    def choose_option(self):
        user_input = input("Player, select your choice: 1 - Rock, 2 - Scissors, 3 - Paper, 4 - Lizard, 5 - Spock: ")
        if(user_input == "1"):
            self.choice = "Player one chose: Rock"
            print(self.choice)
        elif(user_input =="2"):
            self.choice = "Player one chose: Scissors"
            print(self.choice)
        elif(user_input == "3"):
            self.choice = "Player one chose: Paper"
            print(self.choice)
        elif(user_input == "4"):
            self.choice = "Player one chose: Lizard"
            print(self.choice)
        elif(user_input == "5"):
            self.choice = "Player one chose: Spock"
            print(self.choice)
        else:
            print("That is not a valid number, please select a number between 1-5.")

        
        #ADD IN IF STATEMENT 