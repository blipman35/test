from classes import Board
from classes import Player
from classes import Computer
movenum = 0
winner = ""

b = Board()

p = Player(b.board_values)
c = Player(b.board_values)
bv = b.board_values
computer = Computer(c,b,bv)

print("Welcome to Ben's AI tic tac toe game.")
print("You are X and the computer is O.")
print("You will enter a move number from 1-9 starting at the top left of the board")
start = "0"
while start != "1":
    start = input("Press 1 to start:")

if start == '1':
    while movenum < 9 and winner == "":
        p.playermove()
        print("")
        print("Your move")
        b.drawboard()
        movenum += 1
        if computer.testwin('x') == 'yes':
            winner = 'human'

        if movenum < 9 and winner == "":
            computer.computermove('o', 'x')
            print("")
            print("My move")
            b.drawboard()
            movenum += 1
            if computer.testwin('o') == 'yes':
                winner = 'computer'

    if winner == "":
        print("It is a tie!")
    else:
        print("The winner is " + str(winner))

else:
    print("Please press 1:")
