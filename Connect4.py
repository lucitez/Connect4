import random

class Board:
    def __init__(self, width, height):
        '''constructor for the Board class
        '''
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

    def __repr__(self):
        '''repr function allows the printing of the class Board
        '''
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s+= '\n'
        n = -1
        s += '-'
        for col in range(self.width):
            s += '--'
        s += '\n'
        for col in range(self.width):
            n+=1
            if n>9:
                n = 0
            s += ' ' + str(n)
        return s


    def addMove(self, col, ox):
        '''Adds a move to the board, X or O depending on which character is
        going
        '''
        assert(ox == 'X' or ox == 'O')
        for row in range(self.height):
            if self.data[row][col] != ' ':
                break
        if self.data[row][col] != ' ':
            self.data[row-1][col] = ox
        else:
            self.data[row][col] = ox

    def clear(self):
        '''Clears the board
        '''
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def setBoard(self, moveString):
        """ Takes in a string of columns and places alternating
            checkers in those columns, starting with 'X'.

            For example, call board.setBoard('0123456') to see 'X's and
            'O's alternate on the bottom row, or
            board.setBoard('000000') to see them alternate in the left
            column.

            moveString must be a string of integers.
        """
        nextChar = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextChar)
            if nextChar == 'X':
                nextChar = 'O'
            else:
                nextChar = 'X'

    def isMoveLegal(self, col):
        '''Checks a move to see whether a move is out of range or if the column is already
        full
        '''
        if col > self.width-1 or col < 0:
            return False
        else:
            if self.data[0][col] == ' ':
                return True
            else:
                return False

    def isFull(self):
        '''Tests to see if the board is completely filled up
        '''
        for col in range(self.width):
            if self.data[0][col] == ' ':
                return False
        return True
    def deleteMove(self, col):
        '''Removes the top checker from the input column
        '''
        for row in range(self.height):
            if self.data[row][col] != ' ':
                break
        if self.data[row][col] != ' ':
            self.data[row][col] = ' '

    def isWinFor(self, ox):
        '''Checks to see if a player has won, checking each seperate function
        '''
        return self.horizontal(ox) or self.vertical(ox) or self.diagDown(ox) or self.diagUp(ox)

    def horizontal(self, ox):
        '''Checks to see if a player has won horizontally
        '''
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.data[row][col] == self.data[row][col + 1] == \
                   self.data[row][col + 2] == self.data[row][col + 3] == ox:
                    return True
        return False

    def vertical(self, ox):
        '''Checks to see if a player has won vertically
        '''
        for row in range(self.height-3):
            for col in range(self.width):
                if self.data[row][col] == self.data[row+1][col] == \
                self.data[row+2][col] == self.data[row+3][col] == ox:
                    return True
        return False

    def diagDown(self, ox):
        '''Checks to see if a player has won diagonally downwards
        '''
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.data[row][col] == self.data[row+1][col+1] == \
                self.data[row+2][col+2] == self.data[row+3][col+3] == ox:
                    return True
        return False

    def diagUp(self, ox):
        '''Checks to see if a player has won diagonally upwards
        '''
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.data[row][col] == self.data[row-1][col+1] == \
                self.data[row-2][col+2] == self.data[row-3][col+3] == ox:
                    return True
        return False

    def hostGame(self):
        '''Runs the game Connect 4
        '''
        print('Welcome to Connect Four!')
        print(self)
        user = 1
        while True: # loops until the game is won, drawn, or the board is full
            if user%2 == 1:
                col = eval(input('X\'s choice: '))
                if self.isMoveLegal(col) == True:
                    self.addMove(col, 'X')
                    print(self)
                    if self.isWinFor('X'):
                        print('Congratulations X, you win')
                        break
                    elif self.isFull():
                        print('Cat\'s eye!')
                        break
                    else:
                        user +=1
                else:
                    print('Hey, that\'s not right')
            elif user%2 == 0:
                col = eval(input('O\'s choice: '))
                if self.isMoveLegal(col) == True:
                    self.addMove(col, 'O')
                    print(self)
                    user +=1
                else:
                    print('Hey, that\'s not right')
                    col = eval(input('O\'s choice: '))

    def playGame(self, playerX, playerO):
        '''Sets up a game between two AI players
        '''
        print('Welcome to Connect Four!')
        print(self)
        user = 1
        while True:
            if user%2 == 1:
                if playerX == 'human':
                    col = int(input('X\'s choice: '))
                    if self.isMoveLegal(col) == True:
                        self.addMove(col, 'X')
                        print(self)
                        if self.isWinFor('X'):
                            print('Congratulations X, you win')
                            break
                        elif self.isFull():
                            print('Cat\'s eye!')
                            break
                        else:
                            user +=1
                    else:
                        print('Hey, that\'s not right')

                else:
                    col = playerX.nextMove(self)
                    if self.isMoveLegal(col) == True:
                        self.addMove(col, 'X')
                        print(self)
                        if self.isWinFor('X'):
                            print('Congratulations X, you win')
                            break
                        elif self.isFull():
                            print('Cat\'s eye!')
                            break
                        else:
                            user +=1
                    else:
                        print('Hey, that\'s not right')
            elif user%2 == 0:
                if playerO == 'human':
                    col = eval(input('O\'s choice: '))
                    if self.isMoveLegal(col) == True:
                        self.addMove(col, 'O')
                        print(self)
                        if self.isWinFor('O'):
                            print('Congratulations O, you win')
                            break
                        elif self.isFull():
                            print('Cat\'s eye!')
                            break
                        else:
                            user +=1
                    else:
                        print('Hey, that\'s not right')

                else:
                    col = playerO.nextMove(self)
                    if self.isMoveLegal(col) == True:
                        self.addMove(col, 'O')
                        print(self)
                        if self.isWinFor('O'):
                            print('Congratulations O, you win')
                            break
                        elif self.isFull():
                            print('Cat\'s eye!')
                            break
                        else:
                            user +=1
                    else:
                        print('Hey, that\'s not right')

class Player:

    def __init__(self, ox, tiebreakingType, ply):
        """ Constructs a Player object.
        """
        assert(ox == 'X' or ox == 'O')
        assert(tiebreakingType == 'LEFT' or
               tiebreakingType == 'RANDOM' or
               tiebreakingType == 'RIGHT')
        assert(ply >= 0)
        self.ox = ox
        self.tiebreakingType = tiebreakingType
        self.ply = ply

    def __repr__(self):
        """ Creates a string representation of the Player object.
        """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tiebreakingType + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def opponentChecker(self):
        '''Defines an opponent's token as the opposite of the player's token
        '''
        if self.ox == 'X':
            return 'O'
        else:
            return 'X'

    def scoreBoard(self, board):
        '''Returns a value of the board depending on whether there is an
        immediate winner, lose, or none at all.
        '''
        if board.isWinFor(self.ox) == True:
            return '100.0'
        elif board.isWinFor(self.opponentChecker()) == True:
            return '0.0'
        else:
            return '50.0'

    def tiebreakMove(self, scores):
        '''Assigns a column for the next move based on a tiebreak
        '''
        currMax = max(scores)
        highScores = []
        for i in range(len(scores)):
            if scores[i] == currMax:
                highScores += [i]
        if len(highScores) <=1:
            return highScores[0]
        elif self.tiebreakingType == 'LEFT':
            return highScores[0]
        elif self.tiebreakingType == 'RIGHT':
            return highScores[-1]
        else:
            return random.choice(highScores)

    def scoresFor(self, board):
        '''Assigns scores for each column based on a recursive call using the
        amount of ply for the player.
        '''
        scores = [50.0] * board.width
        for col in range(board.width):
            if board.isMoveLegal(col) == False:
                scores[col] = -1.0
            elif board.isWinFor(self.ox) == True:
                scores[col] = 100.0
            elif board.isWinFor(self.opponentChecker()) == True:
                scores[col] = 0.0
            elif self.ply == 0:
                scores[col] = 50.0
            else:
                board.addMove(col, self.ox)
                newP = Player(self.opponentChecker(), self.tiebreakingType, self.ply-1)
                newPScores = newP.scoresFor(board)
                scores[col] = 100.0 - max(newPScores)
                board.deleteMove(col)
        return scores

    def nextMove(self, board):
        '''Adds move based on scoresFor and tieBreaker to the assigned column
        '''
        scores = self.scoresFor(board)
        return self.tiebreakMove(scores)





def connect4():
    '''Calls to the game
    '''
    playerX = 'human'
    #playerO = 'human'
    #playerX = Player('X', 'RANDOM', 4)
    playerO = Player('O', 'RANDOM', 4)
    Board.playGame(Board(7,6),playerX, playerO)

connect4()
