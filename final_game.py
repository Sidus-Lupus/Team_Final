#CW AP final game project
import random

location1 = " "
location2 = " "
location3 = " "
location4 = "O"
location5 = "X"
location6 = "O"
location7 = "X"
location8 = "O"
location9 = "X"

def checkLegalMove(location):
    if location == "X" or location == "O":
        return False
    else:
        return True
    
def runComputerMove():
    random(1,9)

def printGameBoard(loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9 ):
    print(f"{loc1} | {loc2} | {loc3}")
    print("--|---|--")
    print(f"{loc4} | {loc5} | {loc6}")
    print("--|---|--")
    print(f"{loc7} | {loc8} | {loc9}")

printGameBoard(location1, location2, location3, location4, location5, location6, location7, location8, location9)