class Knowledge_New(object):
    """description of class"""
    #this is a dictionary based knowledge system where the board state points to a dictionary which has weighted values for the next move.

    def __init__(self):
        #example of how the nested dictionary system works.
        exampleLayeredDict = {"Dict1":{"text from dict1":100,
                                       "dict1key2":100
                                       },
                              "Dict2":{"text from dict2":100}
            }
        exampleLayeredDict["Dict1"]["newKey"] = "new value"
        #print(exampleLayeredDict["Dict1"])
        
        self.addToThisDict = {
            }

    def add(self, scannedMove, madeMove):
        madeMove = str(madeMove)

        #so what happens here, is that it attempts to find if a particular move has been made before, if it hasnt it will give it the default
        #weighting of 100
        try:
            tempDict = self.addToThisDict[scannedMove]
            try:
                tempWeight = tempDict[madeMove]
            except:
                tempDict[madeMove] = 100

        except:
            tempDict = {}
            tempDict[madeMove] = 100
            self.addToThisDict[scannedMove] = tempDict

    def get(self, x):
        print ("")

    def mutateWeight(self, moveList, win):
        if (win == 0):
            for pair in moveList:
                self.addToThisDict[pair[0]][str(pair[1])] += 8
                #add weighting for wins
        elif (win == 1):
            for pair in moveList:
                self.addToThisDict[pair[0]][str(pair[1])] -= 25
                #subtract weighting for losses
        else:
            for pair in moveList:
                self.addToThisDict[pair[0]][str(pair[1])] += 2
                #small increase for draws
        
    def display(self):
        print ("This will display the board state with all following moves that are known by the AI")
        print("The moves with a higher number are more successful than those with lower numbers")
        print("The numbers 0-8 correspond to 0-8 on the board")
        print("")
        for x in self.addToThisDict:
            print ("Board state:\n", x)
            for y in self.addToThisDict[x]:
                print(y,":",self.addToThisDict[x][y])
            print ("")
        
    def getKnowledge(self, boardState):
        #better name would be showKnowledge
        try:
            print ("\nThese are the known following moves for the given board state")
            print ("The moves with higher weighting are more successful")
            print("The numbers 0-8 correspond to 0-8 on the board")
            for y in self.addToThisDict[boardState]:
                print(y,":",self.addToThisDict[boardState][y])
        except:
            print("There was an error retrieving knowledge\n")