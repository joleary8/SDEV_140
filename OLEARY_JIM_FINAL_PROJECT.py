import random

SIZE = 100
xCordinateLetters = "ABCDEFGHIJ"
xCordinateLetters2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def createPlayerBoard():
    SIZE = 100
    sub = 1
    board = ["0"]
    while sub <= SIZE:
        board.append(".")  # turn on for the real board
        # board.append(sub)  #cheat to show the numbers of the board
        sub += 1
    return board

def placeEnemyShips(board):
    # Adding ships the enemy:
    """
    ship1 = 1,1
    ship2 = 2,2,2
    ship3 = 3,3,3,3
    ship4 = 4,4,4,4,4
    """
    shipPlaced = False
    # ship 1
    while shipPlaced == False:
        orientation = random.randint(1, 2) # Horizontal = 1, Vertical = 2
        bowPoint = random.randint(1, 100)  # Random spot on the board for the bow of the ship

        # Horizontal setup
        if orientation == 1:
            if bowPoint % 10 == 0:
                print("this should only happen when bowPoint is a 10s number, bowPoint:", bowPoint)
            else:
                board[bowPoint] = "1"
                board[(bowPoint + 1)] = "1"
                shipPlaced = True

        # Vertical setup
        if orientation == 2:
            if bowPoint + 10 > 100:
                print("this should only happen when bowPoint is on the bottom row for vertical", bowPoint)
            else:
                board[bowPoint] = "1"
                board[bowPoint + 10] = "1"
                shipPlaced = True
    return board

def printPlayerBoard(board):
    SIZE = 100
    sub = 1
    num = 1
    xCordinateLetters = "ABCDEFGHIJ"
    print(" ", end="")
    for letter in xCordinateLetters:
        print("%5s" % letter, end="")
    print("")

    yCordinateNumbers = 1

    while sub <= SIZE:
        if num == sub:
            print(yCordinateNumbers, end="")
            yCordinateNumbers += 1
            num += 10
        if sub == 91:
            print("%4s" % board[sub], end="")
            sub += 1

        if sub % 10 == 0:
            print("%5s" % board[sub])
            sub += 1
        else:
            print("%5s" % board[sub], end="")
            sub += 1
    return


# Setting up the board
playerBoard = createPlayerBoard()
aiBoard = list(playerBoard)
aiBoard = placeEnemyShips(aiBoard)
print("aiBoard list   ", aiBoard)  # turn off for final version
print("playerBoard list", playerBoard) # turn off for final version
print("AI Board")  # turn off for final version
printPlayerBoard(aiBoard) # turn off for final version
printPlayerBoard(playerBoard)

# PLAYING THE GAME
playing = True
while playing:
    sub = 0
    coordinates = ["A",1]
    print("Enter your X and Y coordinates to ATTACK!")
    coordinates[0] = input("X: ")
    xInputCheck = True
    while xInputCheck:
        if coordinates[0].upper() not in xCordinateLetters2:
            print("Must enter a letter A - J")
            coordinates[0] = input("X: ")
        else:
            coordinates[0] = xCordinateLetters.index(coordinates[0]) + 1
            break

    coordinates[1] = int(input("Y: "))
    print("FIRE!")

    location = coordinates[0] + (coordinates[1] * 10 - 10)
    if aiBoard[location] != "." and aiBoard[location] != "O":
        print("You got a hit!")
        sunkCheck = aiBoard[location]
        aiBoard[location] = "x"
        playerBoard[location] = "x"
        print("sunkCheck after location changed to x", sunkCheck)
        if sunkCheck not in aiBoard:
            print("You sunk a battleship!")

    if playerBoard[location] == "." or playerBoard[location] == "O":
        print("MISSED!")
        playerBoard[location] = "O"
    printPlayerBoard(playerBoard)





