import random

def findBowPoint(aiBoard, shipNumber, orientation):
    """Randomly picks a spot on the board and based on the orientation sent to the function will see if all the required
    spaces for the ship are available. """
    bowPointFound = False
    while not bowPointFound:
        bowPoint = random.randint(1, 100)  # Random spot on the board for the bow of the ship

        # Horizontal ships have an orientation of 1
        # These if statements check that all needed spaces to place the ship are unoccupied.
        if orientation == 1:
            if shipNumber == 1:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 1] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False
            if shipNumber == 2:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 1] == "." \
                        and aiBoard[bowPoint + 2] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False
            if shipNumber == 3:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 1] == "." \
                        and aiBoard[bowPoint + 2] == "." \
                        and aiBoard[bowPoint + 3] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False
            if shipNumber == 4:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 1] == "." \
                        and aiBoard[bowPoint + 2] == "." \
                        and aiBoard[bowPoint + 3] == "."\
                        and aiBoard[bowPoint + 4] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False

        # Vertical Ships have an orientation of 2
        # These if statements check that all needed spaces to place the ship are unoccupied.
        if orientation == 2:
            if shipNumber == 1:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 10] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False
            if shipNumber == 2:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 10] == "." \
                        and aiBoard[bowPoint + 20] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False
            if shipNumber == 3:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 10] == "." \
                        and aiBoard[bowPoint + 20] == "." \
                        and aiBoard[bowPoint + 30] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False
            if shipNumber == 4:
                if aiBoard[bowPoint] == "." and aiBoard[bowPoint + 10] == "." \
                        and aiBoard[bowPoint + 20] == "." \
                        and aiBoard[bowPoint + 30] == "."\
                        and aiBoard[bowPoint + 40] == ".":
                    bowPointFound = True
                else:
                    bowPointFound = False
    return bowPoint

def placeEnemyShips(aiBoard, shipNumber):
    """Randomly picks horizontal or vertical orientation of the ship to be placed on the ai board. Calls findBowPoint
    function to ensure the spaces are clear then checks to make sure the piece can logically fit on the board. (ie even
    though on the list the points for A10 and B1 are next to each other a ship cannot use both those points.)"""
    shipPlaced = False
    i = 0
    orientation = random.randint(1, 2) # Horizontal ships = 1, Vertical ships = 2
    # orientation = 1  # cheat to always have horizontal for testing, change to 2 to always have vertical
    #                    must comment out orientation line using random to use this cheat
    if orientation == 1:
        while not shipPlaced:
            if str(shipNumber) in aiBoard:
                break
            bowPoint = findBowPoint(aiBoard, shipNumber, orientation)

            # This checks that a ship wrap around from the end of one row to the beginning of the row below.
            if (bowPoint >= 1 and bowPoint <= 10 - shipNumber) or  \
               (bowPoint >= 11 and bowPoint <= 20 - shipNumber) or \
               (bowPoint >= 21 and bowPoint <= 30 - shipNumber) or \
               (bowPoint >= 31 and bowPoint <= 40 - shipNumber) or \
               (bowPoint >= 41 and bowPoint <= 50 - shipNumber) or \
               (bowPoint >= 51 and bowPoint <= 60 - shipNumber) or \
               (bowPoint >= 61 and bowPoint <= 70 - shipNumber) or \
               (bowPoint >= 71 and bowPoint <= 80 - shipNumber) or \
               (bowPoint >= 81 and bowPoint <= 90 - shipNumber) or \
               (bowPoint >= 91 and bowPoint <= 100 - shipNumber):
                if i <= shipNumber:
                    aiBoard[bowPoint] = str(shipNumber)
                    if shipNumber == 1:
                        shipPlaced = True
                    i += 1
                if i <= shipNumber:
                    aiBoard[(bowPoint + i)] = str(shipNumber)
                    if shipNumber == 1:
                        shipPlaced = True
                    i += 1
                if i <= shipNumber:
                    aiBoard[(bowPoint + i)] = str(shipNumber)
                    if shipNumber == 2:
                        shipPlaced = True
                    i += 1
                if i <= shipNumber:
                    aiBoard[(bowPoint + i)] = str(shipNumber)
                    if shipNumber == 3:
                        shipPlaced = True
                    i += 1
                if i <= shipNumber:
                    aiBoard[(bowPoint + i)] = str(shipNumber)
                    if shipNumber == 4:
                        shipPlaced = True
                    i += 1
                shipNumber += 1
            else:
                shipPlaced = False
                placeEnemyShips(aiBoard, shipNumber)

    if orientation == 2:
        while not shipPlaced:
            if str(shipNumber) in aiBoard: # This makes sure if a ship is placed a second ship of the same size cannot
                                           # be placed.
                break
            bowPoint = findBowPoint(aiBoard, shipNumber, orientation)

            # These if statements check that a ship does not place any points below the last row.
            if shipNumber == 1:
                if (bowPoint <= 90):
                    aiBoard[bowPoint] = str(shipNumber)
                    aiBoard[(bowPoint + 10)] = str(shipNumber)
                    shipPlaced = True
            if shipNumber == 2:
                if (bowPoint <= 80):
                    aiBoard[bowPoint] = str(shipNumber)
                    aiBoard[(bowPoint + 10)] = str(shipNumber)
                    aiBoard[(bowPoint + 20)] = str(shipNumber)
                    shipPlaced = True
            if shipNumber == 3:
                if (bowPoint <= 70):
                    aiBoard[bowPoint] = str(shipNumber)
                    aiBoard[(bowPoint + 10)] = str(shipNumber)
                    aiBoard[(bowPoint + 20)] = str(shipNumber)
                    aiBoard[(bowPoint + 30)] = str(shipNumber)
                    shipPlaced = True
            if shipNumber == 4:
                if (bowPoint <= 60):
                    aiBoard[bowPoint] = str(shipNumber)
                    aiBoard[(bowPoint + 10)] = str(shipNumber)
                    aiBoard[(bowPoint + 20)] = str(shipNumber)
                    aiBoard[(bowPoint + 30)] = str(shipNumber)
                    aiBoard[(bowPoint + 40)] = str(shipNumber)
                    shipPlaced = True
            else:
                shipPlaced = False
                placeEnemyShips(aiBoard, shipNumber)
    return aiBoard
