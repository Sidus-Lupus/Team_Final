#CW AP final game project
import random

board_setup = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def checkLegalMove(location):
    if board_setup[location-1] == " ":
        return True
    else:
        return False

def playerMove(move):
    if checkLegalMove(move):
        board_setup[move-1] = "X"
        return False
    else:
        return True

def computerMove(move):
    if checkLegalMove(move):
        board_setup[move-1] = "O"
        return False
    else:
        return True
    
def printGameBoard(loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9 ):
    print(f" {loc1} | {loc2} | {loc3}")
    print("---|---|---")
    print(f" {loc4} | {loc5} | {loc6}")
    print("---|---|---")
    print(f" {loc7} | {loc8} | {loc9}")

def printWinner(location):
    if location == "X":
        print("Player Wins!")
    elif location == "O":
        print("Computer Wins!")
    else:
        print("Cat's Game...")

def checkWinner(loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9):
    if loc1 == loc2 == loc3 and loc1 != " ":
        printWinner(loc1)
        return False
    elif loc1 == loc5 == loc9 and loc1 != " ":
        printWinner(loc1)
        return False
    elif loc1 == loc4 == loc7 and loc1 != " ":
        printWinner(loc1)
        return False
    elif loc2 == loc5 == loc8 and loc2 != " ":
        printWinner(loc2)
        return False
    elif loc3 == loc6 == loc9 and loc3 != " ":
        printWinner(loc3)
        return False
    elif loc3 == loc5 == loc7 and loc3 != " ":
        printWinner(loc3)
        return False
    elif loc1 != " " and loc2 != " " and loc3 != " " and loc4 != " " and loc5 != " " and loc6 != " " and loc7 != " " and loc8 != " " and loc9 != " ":
        print("Cat's Game...")
        return False
    else:
        return True
       
while checkWinner(board_setup[0], board_setup[1], board_setup[2], board_setup[3], board_setup[4], board_setup[5], board_setup[6], board_setup[7], board_setup[8]):
    printGameBoard(board_setup[0], board_setup[1], board_setup[2], board_setup[3], board_setup[4], board_setup[5], board_setup[6], board_setup[7], board_setup[8])
    while playerMove(int(input("Where would you like to play (1-9 left-right then top-down)?: "))):
        pass
    while computerMove(random.randint(1,9)):
        pass
printGameBoard(board_setup[0], board_setup[1], board_setup[2], board_setup[3], board_setup[4], board_setup[5], board_setup[6], board_setup[7], board_setup[8])