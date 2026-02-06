#CW AP final game project

location1 = "X"
location2 = "O"
location3 = "X"
location4 = "O"
location5 = "X"
location6 = "O"
location7 = "X"
location8 = "O"
location9 = "X"

def printGameBoard(loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9 ):
    print(f"{loc1} | {loc2} | {loc3}")
    print("--|---|--")
    print(f"{loc4} | {loc5} | {loc6}")
    print("--|---|--")
    print(f"{loc7} | {loc8} | {loc9}")

def findBoardLocation(location):
    if location == 1:
        return location1
    elif location == 2:
        return location2
    elif location == 3:
        return location3
    elif location == 4:
        return location4
    elif location == 5:
        return location5
    elif location == 6:
        return location6
    elif location == 7:
        return location7
    elif location == 8:
        return location8
    else:
        return location9

printGameBoard(location1, location2, location3, location4, location5, location6, location7, location8, location9)
def playerMove(move):
    int(input(f"where would you like to play (1-9 left-right then top-down)?: "))
    if
    location == "X"