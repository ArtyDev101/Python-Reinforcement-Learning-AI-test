import random

class AI_Player(object):
    """
    This is an experimental class that runs on a weighted algorithmn.
    """
    def __init__(self, Knowledge):
        self.knowledge = Knowledge

    def makeMove(self, Board):
        #gain a list of all possible moves to be made by iterating through the board
        possibleMovesArray = []
        roundsCounter = 0
        boardState = Board.getState()
        print ("AI_TEST is making a move")
        for i in Board.board:
            for x in i:
                if not (x):
                    possibleMovesArray.append(roundsCounter)
                    roundsCounter += 1
                else:
                    roundsCounter += 1 
        try:
            tempDict = self.knowledge.addToThisDict[boardState]
            newDict = {}
            for x in possibleMovesArray:
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
                    self.addKnowledge(boardState, possibleMovesArray[count])
                    return possibleMovesArray[count]
                else:
                    count += 1

        except:
            myRandom = random.choice(possibleMovesArray)
            madeMove = str(myRandom)
            self.addKnowledge(boardState, madeMove)
            return myRandom

    def makeMoveRandom(self, Board):
        possibleMovesArray = []
        roundsCounter = 0
        print ("AI_TEST is making a move")
        for row in Board.board:
            for x in row:
                if not (x):
                    possibleMovesArray.append(roundsCounter)
                    roundsCounter += 1
                else:
                    roundsCounter += 1
        myRandom = random.choice(possibleMovesArray)
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