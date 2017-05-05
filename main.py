from classes import Board
from classes import Player
from classes import Computer
gameover = False

b = Board()

p = Player(b.board_values)
c = Player(b.board_values)
bv = b.board_values
b.drawboard()
computer = Computer(c,b,bv)

# while gameover is False:
#     p.playermove()
#     b.drawboard()

computer.computermove('o', 'x')
