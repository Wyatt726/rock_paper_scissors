class Player:
    def __init__(self):
        self.player_name = ''
        self.gesture_list =["","",""]

    def assign_name(self, player_number_str):
        self.player_name = input('Enter the name for player ' + player_number_str)

        #  player = input("rock,paper,scissors, lizard or spock?:").lower()
    
        