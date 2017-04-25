import turtle

class Board:#this class contains everything that is a part of the tic tac toe board

    def __init__(self):
        self.u__init_board = []

    def drawboard(self):
        #This method will draw the tic tac toe board for the game to be played
        t=turtle.Turtle()
        t.ht()
        t.up()
        t.goto(-40,-40)
        t.down()
        t.forward(240)
        t.left(90)
        t.forward(240)
        t.left(90)
        t.forward(240)
        t.left(90)
        t.forward(80)
        t.left(90)
        t.forward(240)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(240)
        t.left(90)
        t.goto(-40,-40)
        t.left(180)
        t.forward(160)
        t.up()
        t.goto(40,-40)
        t.down()
        t.forward(240)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(240)
