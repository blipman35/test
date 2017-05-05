from classes import Board
from classes import Player
from classes import Computer
movenum = 0

b = Board()

p = Player(b.board_values)
c = Player(b.board_values)
bv = b.board_values
computer = Computer(c,b,bv)

while movenum < 9:
    p.playermove()
    print("")
    print("Your move")
    b.drawboard()
    movenum += 1

    if movenum < 9:
        computer.computermove('o', 'x')
        print("")
        print("My move")
        b.drawboard()
        movenum += 1
