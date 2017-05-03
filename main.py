from classes import Board

gameover = False

b = Board()
b.newboard()
b.drawboard()

while gameover is False:
    b.move()
    b.drawboard()

b.computermove()
