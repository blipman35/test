class Board(object):

    global gameover


    def __init__(self):
        #Setup a 9 element array to represent the board
        self.board_values = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


    def drawboard(self):
        #print out the board
        x = self.board_values
        print(" " + x[0] + " " + "|" + " " + x[1] + " " + "|" + " " + x[2])
        print("-----------")
        print(" " + x[3] + " " + "|" + " " + x[4] + " " + "|" + " " + x[5])
        print("-----------")
        print(" " + x[6] + " " + "|" + " " + x[7] + " " + "|" + " " + x[8])

class Player:

    def __init__(self, bv):
        self.board_values = bv


    def playermove(self):
        #asks play for move, updates the board
        ask = int(input('Make a move (1-9):'))#ask
        position = ask - 1 #python starts at 0, but the player doesnt know that
        #check for repeated moves
        if self.board_values[position] != '-':
            print("Invalid move")
        else:
            self.board_values[position] = 'x'



class Computer:

    def __init__(self, c, b, bv):
        self.ComputerPlayer = c
        self.board = b
        self.board_values = bv

    def computermove(self):
        #check the rows for winning moves
        for i in range(3):
            row = self.board_values[i*3: (i*3) + 3] #puts each row into a new index
            print('rows')
            print(row)
            if row.count("o") == 2 and row.count("-") == 1: #if any row has two o's and one empty space
                print("i can win") #the computer recognizes that it can win
                self.board_values[position] = 'o'

        column = []

        for i in range(0,3):
            column = []
            column.append(self.board_values[0 + i])
            column.append(self.board_values[3 + i])
            column.append(self.board_values[6 + i])
            print('columns')
            print(column)
            if column.count("o") == 2 and column.count("-") == 1:
                print("i can win")




        diagonal1 = []
        diagonal1.append(self.board_values[0])
        diagonal1.append(self.board_values[4])
        diagonal1.append(self.board_values[8])
        print('diagonals')
        print(diagonal1)

        diagonal2 = []
        diagonal2.append(self.board_values[2])
        diagonal2.append(self.board_values[4])
        diagonal2.append(self.board_values[6])
        print(diagonal2)
