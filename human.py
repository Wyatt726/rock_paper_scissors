from player import Player
class Human(Player):
    def __init__(self):
        self.player_name = None
        super().__init__()

    def choose_option(self):
        user_input = input("Enter the appropriate number for your choice: /n"
             "1 - Rock /n"
             "2 - Scissors /n"
             "3 - Paper /n"
             "4 - Lizard /n"
             "5 - Spock/n")
        if(user_input == "1"):
            self.choice = "Rock"
        elif(user_input =="2"):
            self.choice = "Scissors"
        elif(user_input == "3"):
            self.choice = "Paper"
        elif(user_input == "4"):
            self.choice = "Lizard"
        elif(user_input == "5"):
            self.choice = "Spock"
        #ADD IN IF STATEMENT 