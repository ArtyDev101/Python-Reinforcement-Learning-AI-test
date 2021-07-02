import random

class AI_CONTROL(object):
    """
    This is a control class that randomly places moves
    """
    def __init__(self):
        print("")

    def makeMove(self, Board):
        possibleMoves = []
        counter = 0
        print ("AI_CONTROL is making a move")
        for i in Board.board:
            for x in i:
                if not (x):
                    possibleMoves.append(counter)
                    counter += 1
                else:
                    counter += 1
        return random.choice(possibleMoves)

    #this code searches the board for empty cells, which denotes a possible move before returning a random possible move.