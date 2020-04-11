class Player:
    def __init__(self, name, token): 
        self.name = name 
        self.token = token
    
# p1 = Player("player_one", "x")
# p2 = Player("player_two", "y")

class Game:
    def __init__(self, board): 
        self.board = board

board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

