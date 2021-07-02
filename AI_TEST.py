import random

class AI_TEST(object):
    """
    This is an experimental class that runs on a weighted algorithmn.
    """
    def __init__(self, Knowledge):
        self.knowledge = Knowledge

    def makeMove(self, Board):
        #gain a list of all possible moves to be made by iterating through the board
        possibleMoves = []
        counter = 0
        boardState = Board.getState()
        print ("AI_TEST is making a move")
        for i in Board.board:
            for x in i:
                if not (x):
                    possibleMoves.append(counter)
                    counter += 1
                else:
                    counter += 1 
        try:
            tempDict = self.knowledge.addToThisDict[boardState]
            newDict = {}
            for x in possibleMoves:
                newDict[str(x)] = 100
            for key, value in tempDict.items():
                newDict[key] = value
            sum = 0
            for i in list(newDict.values()):
                sum += i
            weightedSelection = random.randint(0,sum)
            count = 0
            for x in list(newDict.values()):
                weightedSelection -= x
                if (weightedSelection <= 0):
                    self.addKnowledge(boardState, possibleMoves[count])
                    return possibleMoves[count]
                else:
                    count += 1

        except:
            myRandom = random.choice(possibleMoves)
            madeMove = str(myRandom)
            self.addKnowledge(boardState, madeMove)
            return myRandom

    def makeMoveRandom(self, Board):
        possibleMoves = []
        counter = 0
        print ("AI_TEST is making a move")
        for i in Board.board:
            for x in i:
                if not (x):
                    possibleMoves.append(counter)
                    counter += 1
                else:
                    counter += 1
        myRandom = random.choice(possibleMoves)
        madeMove = str(myRandom)
        self.addKnowledge(boardState, madeMove)
        return myRandom
        
    def addKnowledge(self, scannedMove, madeMove):
        self.knowledge.add(scannedMove, madeMove)

    def mutateWeight(self, moveList, win):
        self.knowledge.mutateWeight(moveList, win)

    def displayKnowledge(self):
        self.knowledge.display()

    def getKnowledge(self, boardState):
        self.knowledge.getKnowledge(boardState)