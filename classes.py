

class Board(object):

    global movenum
    global winner

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

    def __init__(self, bv): #allows you to use board_values in the Player class
        self.board_values = bv


    def playermove(self):
        #asks play for move, updates the board
        ask = int(input('Make a move (1-9):'))
        position = ask - 1 #python starts at 0, but the player doesnt know that
        #check for repeated moves
        if self.board_values[position] != '-':
            print("Invalid move")
            self.playermove()
        else:
            self.board_values[position] = 'x'




class Computer:

    def __init__(self, c, b, bv): #allows you to use board_values, board, and the computerplayer in Computer
        self.ComputerPlayer = c
        self.board = b
        self.board_values = bv

    def computermove(self, computer_id, human_id):
        #check to see if the computer has a winning move
        i = self.winningmove(computer_id)
        #Check to see if the player has a winning move next
        j = self.winningmove(human_id)

        if i is not None:
            #make the winning move
            self.board_values[i] = computer_id
        elif j is not None:
            #make move to block the players winning move
            self.board_values[j] = computer_id
        else:
            if self.nextmove(computer_id) is not None:
                k = self.nextmove(computer_id)
                self.board_values[k] = computer_id
            else:
                k = self.board_values.index('-')
                self.board_values[k] = computer_id

    def winningmove(self, player_id):
        #check the rows for winning moves
        for i in range(3):
            row = self.board_values[i*3: (i*3) + 3] #puts each row into a new index
            if row.count(player_id) == 2 and row.count("-") == 1: #if any row has two o's and one empty space
                move = (3*i) + row.index('-')
                return(move)

        column = []
        for i in range(0,3):
            #Allows the computer to recognize the 3 columns of the tic tac toe board
            column = []
            column.append(self.board_values[0 + i])
            column.append(self.board_values[3 + i])
            column.append(self.board_values[6 + i])
            if column.count(player_id) == 2 and column.count("-") == 1:
                #If there is a winning move in a column, computer makes the move.
                move = (i) + (3*column.index('-'))
                return(move)

        diagonal1 = []
        #Allows for the computer to recognize the first diagonal (top left corner to bottom right corner)
        diagonal1.append(self.board_values[0])
        diagonal1.append(self.board_values[4])
        diagonal1.append(self.board_values[8])
        if diagonal1.count(player_id) == 2 and diagonal1.count("-") == 1:
            #If there is a winning move in the first diagonal, computer makes the move.
            move = (4*diagonal1.index('-'))
            return(move)

        diagonal2 = []

        #Allows for the computer to recognize the second diagonal (top right corner to bottom left corner)
        diagonal2.append(self.board_values[2])
        diagonal2.append(self.board_values[4])
        diagonal2.append(self.board_values[6])
        if diagonal2.count(player_id) == 2 and diagonal2.count("-") == 1:
            #If there is a winning move in the second diagonal, computer makes the move.
            move = 2 + (2 * diagonal2.index('-'))
            return(move)

    def testwin(self, player_id):
        #check the rows for winning moves
        for i in range(3):
            row = self.board_values[i*3: (i*3) + 3] #puts each row into a new index
            if row.count(player_id) == 3:
                #if the computer or the player have three in a row
                return('yes')

        column = []

        for i in range(0,3):
            column = []
            column.append(self.board_values[0 + i])
            column.append(self.board_values[3 + i])
            column.append(self.board_values[6 + i])
            if column.count(player_id) == 3:
                #if the computer or the player have three in a column
                return('yes')

        diagonal1 = []

        diagonal1.append(self.board_values[0])
        diagonal1.append(self.board_values[4])
        diagonal1.append(self.board_values[8])
        if diagonal1.count(player_id) == 3:
            #if the computer or the player have three in the first diagonal
            return('yes')

        diagonal2 = []

        diagonal2.append(self.board_values[2])
        diagonal2.append(self.board_values[4])
        diagonal2.append(self.board_values[6])
        if diagonal2.count(player_id) == 3:
            #if the computer or the player have three in the second diagonal
            return('yes')

    def nextmove(self, player_id):
        #check the rows for winning moves
        for i in range(3):
            row = self.board_values[i*3: (i*3) + 3] #puts each row into a new index
            if row.count(player_id) == 1 and row.count("-") == 2:
                #if a row has two empty spaces, make a move in that row
                move = (3*i) + row.index('-')
                return(move)

        column = []
        for i in range(0,3):
            column = []
            column.append(self.board_values[0 + i])
            column.append(self.board_values[3 + i])
            column.append(self.board_values[6 + i])
            if column.count(player_id) == 1 and column.count("-") == 2:
                #if a column has two empty spaces, make a move in that column
                move = (i) + (3*column.index('-'))
                return(move)

        diagonal1 = []

        diagonal1.append(self.board_values[0])
        diagonal1.append(self.board_values[4])
        diagonal1.append(self.board_values[8])
        if diagonal1.count(player_id) == 1 and diagonal1.count("-") == 2:
            #if the first diagonal has two empty spaces, make a move in that diagonal
            move = (4*diagonal1.index('-'))
            return(move)

        diagonal2 = []

        diagonal2.append(self.board_values[2])
        diagonal2.append(self.board_values[4])
        diagonal2.append(self.board_values[6])
        if diagonal2.count(player_id) == 1 and diagonal2.count("-") == 2:
            #if the second diagonal has two empty spaces, make a move in that diagonal
            move = 2 + (2 * diagonal2.index('-'))
            return(move)
