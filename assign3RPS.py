# Rock, Paper, Scissors Game made for two players
import random

# number of games and scores start at 0 
games = 0
onescore = 0
twoscore = 0

# defining a function with the parameters where player one win or where player 2 wins
def winner(playerOne, playerTwo):
    if (playerOne == "R" or playerOne == "r") and (playerTwo == "P" or playerTwo == "p"):
        return 2
    elif (playerOne == "P" or playerOne == "p") and (playerTwo == "S" or playerTwo == "s"):
        return 2
    elif (playerOne == "S" or playerOne == "s") and (playerTwo == "R" or playerTwo == "r"):
        return 2
    elif (playerOne == "R" or playerOne == "r") and (playerTwo == "S" or playerTwo == "s"):
        return 1
    elif (playerOne == "P" or playerOne == "p") and (playerTwo == "R" or playerTwo == "r"):
        return 1
    elif (playerOne == "S" or playerOne == "s") and (playerTwo == "P" or playerTwo == "p"):
        return 1
    # returns a zero if the players tie
    return 0

# Players have 5 rounds to win
while games < 5:
    # Asks player one for their selection in either uppercase or lowercase
    playerOne = None
    while playerOne != "R" and playerOne != "r" and playerOne != "P" and playerOne != "p" and playerOne != "S" and playerOne != "s":
        print("Player 1: Please enter either (R)ock, (P)aper, or (S)cissors:")
        playerOne = input()
        
    # Asks player two for their selection in either uppercase or lowercase
    playerTwo = None
    while playerTwo != "R" and playerTwo != "r" and playerTwo != "P" and playerTwo != "p" and playerTwo != "S" and playerTwo != "s":
        print("Player 2: Please enter either (R)ock, (P)aper, or (S)cissors:")
        playerTwo = input()
        
    # Storing the result of the function
    winnerResults = winner(playerOne, playerTwo)
    # Using winner results it says who wins and increments the winners score
    if winnerResults == 1:
        print("Player 1 wins.")
        onescore = onescore + 1
    elif winnerResults == 2:
        print("Player 2 wins.")
        twoscore = twoscore + 1
    elif winnerResults == 0:
        print("Nobody wins.")
    # Shows the results 
    print("Scores after this play:")
    print("Player 1:", + onescore)
    print("Player 2:", + twoscore)
    # increments number of games played
    games = games + 1


        
    
    
