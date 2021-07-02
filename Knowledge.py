class Knowledge(object):
    """description of class"""
    #255168 possible states for a noughts and crosses game
    #26830 if symmetries are taken into account

    def __init__(self):
        self.knowledgeMoves = []
        self.firstMoveWeight = { 0 : 100,\
            1 : 100,\
            2 : 100,\
            3 : 100,\
            4 : 100,\
            5 : 100,\
            6 : 100,\
            7 : 100,\
            8 : 100}
        #add default knowledge
        self.knowledgeMoves.append([["x",4],["o",7],["x",2],["o",8],["x",6],["win"]])
        self.firstMoveWeight[4] += 0

    #stable numbers for use in weighting, 10, 6, 1
    #currently using the harsher 10,8,1
    def add(self, Knowledge):
        self.knowledgeMoves.append(Knowledge)
        if (Knowledge[len(Knowledge)-1][0] == "win"):
            self.firstMoveWeight[Knowledge[0][1]] += (10 - (len(Knowledge)-1))
        elif (Knowledge[len(Knowledge)-1][0] == "loss"):
            if (self.firstMoveWeight[Knowledge[0][1]] > 8):
                self.firstMoveWeight[Knowledge[0][1]] -= 8
        else:
            if (self.firstMoveWeight[Knowledge[0][1]] > 1):
                self.firstMoveWeight[Knowledge[0][1]] -= 1
        print ("Weighting: ", self.firstMoveWeight)
