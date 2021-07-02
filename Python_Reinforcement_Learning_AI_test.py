"""
This is a reinforcement learning based approach to the problem.

Author: Junior McGrath

As a part of BSC Computer Science at the University of Westminster
"""

#import of classes required for functionality
from AI_TEST import AI_TEST
from AI_CONTROL import AI_CONTROL
from Board import Board
from Knowledge import Knowledge
from Knowledge_New import Knowledge_New

#honestly my favorite module, allows time functions like sleep() and counting time 
import time

print ("AI Testing program commenced execution. \n")
print ("This is Version 0.1.2, please refer to another source for other versions")

#function that prints the data after a match has concluded. Shown includes Time taken for match to complete,(To be used to determine how fast the iterations can run on different PCs)
#Number of iterations, and the % the Learning player has Won/Lost/Drawn
def printMatchStats(timeStart, iterationCounter, wins, losses, draws):
    timeEnd = time.perf_counter()
    print ("Match finished in: " + str((timeEnd - timeStart) * 1000) + " Milliseconds")
    print ("Completed " + str(iterationCounter) + " iteration(s)")
    print ("Player X has won " + str(round(100 * (wins/(wins + losses + draws)),2)) + "% of matches")
    print ("Player X has lost " + str(round(100 * (losses/(wins + losses + draws)),2)) + "% of matches")
    print ("Player X has drawn " + str(round(100 * (draws/(wins + losses + draws)),2)) + "% of matches")
    print ("")

#Main menu, called once on starting main and called again whenever a menu option is completed.
def showMenu():
    print ("This is the main menu. Please proceed.")

    print("0. Run AI loop")
    print("1. View knowledge base")
    print("2. Lookup knowledge for a board state")
    print("3. Exit")
    option = input("Please enter the corresponding number for your choice. \n")
    #checking the input is called in the code block that calls this function
    return option

#This is where the main logic for the program is
def main():

    #we initialise the main objects that will be used in this code block
    board = Board()
    knowledge = Knowledge_New()
    AI_test = AI_TEST(knowledge)
    AI_control = AI_CONTROL()

    #self explanatory
    iterationCounter = 0
    wins = 0
    losses = 0
    draws = 0

    #Now this is the main logic behind the program
    #This first while loop handles the menu, and has multiple if/elif statements that handle the menu choices
    while True:

        #call the function function that both shows the menu and gets the user choice for menuo options
        menuOption = str(showMenu())
        #Now that I think back on it, it would've been better to just return the input as a string rather than str() it here.

        if menuOption == "0":
            print("\nAI Loop ready to begin, cancel the loop at any time by pressing CTRL + C. Press enter when ready. ")
            waitForEnter = input("")
        #if the user chooses to run the learning loop.
        #This loop works by resetting the board state, and then having both players place moves on the board until a move is considered a winning move
        #upon a win for player x, the wins as incremented, or losses for a loss, etc, then prints the statistic.
        #the made move is saved as "tempknowledge", once the match is completed this tempknowledge holds all the moves made in the game
        #if player x won, then the moves made for the win are given increased weight or decreased if player x lost
        #player o has no knowledge because it is the control used to test.

            try:
                while True:

                    #I use the roundcounter to check when draw by maximum rounds is hit
                    roundCount = 0

                    board.reset()

                    #Used to check how long an iteration takes
                    timeStart = time.perf_counter()
                    iterationCounter += 1

                    #initialise the array used to store the moves made in the game.
                    tempKnowledge = []

                    while True: #This loop represents the single match

                        #pair is a pair of the current boardstate and what move is made
                        pair = []
                        pair.append(board.getState())
                        #this makes up the basis of how the knowledge works. Each boardstate has a weighted selection of possible moves to make
                        
                        #here we have player x make a move and then record it into the tempknowledge array for later
                        AI_Test_Move = AI_test.makeMove(board)
                        pair.append(AI_Test_Move)
                        tempKnowledge.append(pair)

                        roundCount += 1

                        #board.put, other than putting the character on the board also returns True if its a winning move.
                        #Put and board checking should be split up for easier use.
                        if (board.put("x",AI_Test_Move)):
                            print ("Win for player x!")
                            wins += 1

                            #This mutate weight method is what is responsible for increasing/decreasing the weights in the knowledge 
                            #This forms the basis of how the moves to be made are selected.
                            AI_test.mutateWeight(tempKnowledge, 0)
                            printMatchStats(timeStart, iterationCounter, wins, losses, draws)
                            break
                        else:
                            print ("")#newline

                        #if player X's move didnt win we move onto player O, then loop back to player X and so on.
                        roundCount += 1
                        board.getState()
                        if (roundCount < 9):
                            AI_Control_Move = AI_control.makeMove(board)
                            if (board.put("o",AI_Control_Move)):
                                print ("Win for player o!")
                                losses += 1
                                AI_test.mutateWeight(tempKnowledge, 1)
                                printMatchStats(timeStart, iterationCounter, wins, losses, draws)
                                break
                            else:
                                print ("")
                        else:
                            print ("Draw!")
                            draws += 1
                            AI_test.mutateWeight(tempKnowledge, 2)
                            printMatchStats(timeStart, iterationCounter, wins, losses, draws)
                            break
                    print ("")

            except KeyboardInterrupt:
                print("Loop stopped")
                printMatchStats(timeStart, iterationCounter, wins, losses, draws)

        elif menuOption == "1":
            print("\nThis is the complete knowledge base of AI_test")
            AI_test.displayKnowledge()
        elif menuOption == "2":
            print("Enter a board state in the format 000000000, use x, o or 0")
            inputState = input("Enter a state\n")
            AI_test.getKnowledge(inputState)
        elif menuOption == "3":
            print("Program exiting...")
            time.sleep(1)
            break
        else:
            print ("Menu error")




if __name__ == "__main__":
    main()
