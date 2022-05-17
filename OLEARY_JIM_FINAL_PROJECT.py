#Program: OLEARY_JIM_FINAL_PROJECT
#Author: Jim O'Leary
# Python 3.9.7
# Program: A game of Battleship against an AI Board. This version the player has unlimited guesses and does not have a
#           a board of their own. Once they have won the game they are prompted if they want to play again.
# Variables:
#   xCoordinateLetters: single string containing all the x coordinate letters (str)
#   xCoordinateLetters2: a list of the letters as individual strings (tuple)
#   fleetSize: the number of enemy ships to be put on the board (int)
#   playerBoard: a list containing all the positions on the board used to represent the player's board  (list)
#   aiBoard: a list containing all the positions on the board that includes the enemy ships (list)

import placeShips

# uses both a string and a tuple for easier ways to access the data for the columns.
xCoordinateLetters = "ABCDEFGHIJ"
xCoordinateLetters2 = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
fleetSize = 4 # total number of enemy ships to place



def createPlayerBoard():
    """Creates a list that will be used to represent the board. This function is used for both the player's board and
        the ai's board."""
    SIZE = 150 # Makes a list bigger than the board so checking spots outside the board size does not give a
               # list index out of range error.
    sub = 1    # Starts at 1 because the [0] position of the list is not used on the board itself.
    board = ["0"]  # The list starts with a character filled in already at position [0] so that each board piece
                   # corresponds to the subscript of the list (ie point (A,1) = board[1], (J,10) = board[100]
    while sub <= SIZE:
        board.append(".")
        sub += 1
    return board

def printBoard(board, xCordinateLetters):
    """Prints the board to the screen with (X,Y) labels. This function is used for both the player's board and
        the ai's board."""
    SIZE = 100
    sub = 1
    num = 1
    print(" ", end="")
    for letter in xCordinateLetters:
        print("%5s" % letter, end="")
    print("")
    yCordinateNumbers = 1

    while sub <= SIZE:
        # Prints the label for the Y coordinates at the start of each row
        if num == sub:
            print(yCordinateNumbers, end="")
            yCordinateNumbers += 1
            num += 10
        # Changes the spacing for row 10 label because it is 2 digits
        if sub == 91:
            print("%4s" % board[sub], end="")
            sub += 1
        # Makes a new line after printing 10 "." points for the board
        if sub % 10 == 0:
            print("%5s" % board[sub])
            sub += 1
        # Prints the rest of the "." points for the board
        else:
            print("%5s" % board[sub], end="")
            sub += 1
    return

def youWin():
    """Victory message and end of game play again prompt."""
    playAgainList = ["Y", "N"]
    print("Victory!\nYou sunk the fleet!")
    playAgain = input("Would you like to play again? (Y/N) ")
    playAgainCheck = True
    while playAgainCheck:
        if playAgain.upper() not in playAgainList:
            print("Please enter Y or N")
            playAgain = input("Would you like to play again? (Y/N) ")
        else:
            if playAgain.upper() == "Y":
                main()
            if playAgain.upper() == "N":
                print("Goodbye.")
                exit()
            break

def attack(playerBoard, aiBoard):
    """Gets input from the user for where to attack and validates the data. Once data has been validated updates
       playberboard and aiboard lists with the results of the attack."""
    attacking = True
    while attacking:
        coordinates = ["A", 1]
        print("Enter your X and Y coordinates to ATTACK!")
        coordinates[0] = input("X: ").upper()
        xInputCheck = True
        yInputCheck = True

        # Validates the input for X coordinate is only the letters A through J
        while xInputCheck:
            if coordinates[0].upper() not in xCoordinateLetters2:
                print("Must enter a letter A - J")
                coordinates[0] = input("X: ").upper()
            else:
                # Converts the letter coordinate to a number for calculating the position on aiBoard that is being attacked.
                coordinates[0] = xCoordinateLetters.index(coordinates[0]) + 1
                break

        # Validates the input for Y coordinate is only the numbers 1 - 10
        while yInputCheck:
            try:
                coordinates[1] = int(input("Y: "))
                yInputCheck = False
                if coordinates[1] < 1 or coordinates[1] > 10:
                    print("Please enter a number between 1 - 10")
                    yInputCheck = True
            except ValueError:
                print("Please enter a number between 1 - 10")
        print("FIRE!")

        # Calculates the position in aiBoard to attack
        location = coordinates[0] + (coordinates[1] * 10 - 10)

        # Checks the aiBoard to see if a ship is in the position that was attacked.
        if aiBoard[location] != "." and aiBoard[location] != "O":
            print("You got a hit!")
            sunkCheck = aiBoard[location]

            # Changes the spots hit to an "x" on both aiBoard and playerBoard
            aiBoard[location] = "x"
            playerBoard[location] = "x"

            # If the number of the ship hit no longer appears in aiBoard that means the ship was sunk.
            if sunkCheck not in aiBoard:
                print("You sunk a battleship!")

            # If no more numbers appear on aiBoard the game has been won.
            if "1" not in aiBoard and "2" not in aiBoard and "3" not in aiBoard and "4" not in aiBoard:
                youWin()

        if playerBoard[location] == "." or playerBoard[location] == "O":
            print("MISSED!")
            playerBoard[location] = "O"

        # The player board is reprinted after each turn.
        printBoard(playerBoard, xCoordinateLetters)

def playingGame():
    """Calls the functions to create the playerboard and aiboard lists. The aiboard list runs a loop of ships until
    they have all been placed in valid spaces."""
    # Setting up the board
    playerBoard = createPlayerBoard()
    aiBoard = list(playerBoard)

    # Loop through creating the ships.
    shipNumber = 1
    while shipNumber <= fleetSize:
        aiBoard = placeShips.placeEnemyShips(aiBoard, shipNumber)
        shipNumber += 1

    #print("AI Board")  # Label for cheat on next line
    #printBoard(aiBoard, xCordinateLetters)  # Cheat to show where the enemy ships are placed, used for testing
    printBoard(playerBoard, xCoordinateLetters)

    # Start attack
    attack(playerBoard, aiBoard)

def main():
    playingGame()

main()






















