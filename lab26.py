
class Player:
    def __init__(self, name, token): 
        self.nomen = nomen
        self.symbol = symbol
    
# # p1 = Player("player_one", "x")
# # p2 = Player("player_two", "y")

# class Game:
#     def __init__(self, board): 
#         self.board = board

playing = True

champion = None

table = ["...", "...", "...",
        "...", "...", "...",
        "...", "...", "..."]

def visual():
    print(table[0] + " : " + table[1] + " : " + table[2])
    print(table[3] + " : " + table[4] + " : " + table[5])
    print(table[6] + " : " + table[7] + " : " + table[8])

def mechanics(player):
    spot = input("Choose a position between 1 and 9, (starting from the top left)")
    spot_two = int(spot) - 1

    table[spot_two] = "1"
    visual()

def play():

    visual()

    while playing():

        mechanics(current)

        status()

        change()

    if champion == "X" or champion == "0":
        print(champion + "was victious")

    elif champion == None:
        print("Tie!")

def status():

    win()

    tie()

def win():

    global champion

    rose_win = rose()

    call_ems_win = call_ems()

    diagonals_win = diagonals()
    if rose_win = rose()
        champion = rose()

    elif call_ems_win = call_ems()
        champion = call_ems()

    elif diagonals_win = diagonals()
        champion = diagonals()

    else:
        champon = None

    return

#     table = {'1': ' ' , '2': ' ' , '3': ' ' ,
#             '4': ' ' , '5': ' ' , '6': ' ' ,
#             '7': ' ' , '8': ' ' , '9': ' ' }
            
# def visual(table):
#     print(['1'] + '|' + ['2'] + '|' + ['3'])
#     print('-+-+-')
#     print(['4'] + '|' + ['5'] + '|' + ['6'])
#     print('-+-+-')
#     print(['7'] + '|' + ['8'] + '|' + ['9'])

def rose():

    return

def call-ems():

    return

def diagonals():

    return

def tie():
    return

def change():


play()

# while True:
# 	  x = input('Pick a number from 0-10')
# 	  x = int(x)
# 	  board[x] = 'X'
# 	  print(board)