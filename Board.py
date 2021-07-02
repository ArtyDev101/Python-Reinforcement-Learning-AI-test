class Board(object):
    """description of class"""

    board = [[[],[],[]], \
            [[],[],[]], \
            [[],[],[]]]

    boardWidth = 0
    for i in board[0]:
        boardWidth += 1

    def getState(self):
        string = ""
        for row in self.board:
            for item in row:
                if item:
                    string += item
                else:
                    string += "0"
        return string
        #return the state of the board as a string of 9 characters, x, o or 0

    def put(self, character, position):

        x = position//self.boardWidth
        y = position%self.boardWidth
        self.board[x][y] = character

        print("")
        print ("-----" * self.boardWidth)
        for i in range(self.boardWidth):
            print (self.board[i])
        print ("-----" * self.boardWidth)
        print("")

        return self.checkWin(position, character)

    def checkWin(self, position, character):

        win = True

        x = position//self.boardWidth
        y = position%self.boardWidth

        #basically as soon as one of these checks/ which check for 3 matching characters in different ways returns true, then true is returned, denoting a winning move

        for i in self.board[x]:
            if (i != character):
                win = False
        if not (win):
            win = True
            for i in range(self.boardWidth):
                if (self.board[i][y] != character):
                    win = False

        if not (win):
            win = True
            for i in range(self.boardWidth):
                if (self.board[i][i] != character):
                    win = False

        if not (win):
            win = True
            for i in range(self.boardWidth):
                if (self.board[i][self.boardWidth-(i+1)] != character):
                    win = False

        return win

    def reset(self):
        self.board = [[[],[],[]], \
            [[],[],[]], \
            [[],[],[]]]