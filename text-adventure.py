
energy = 10
moves = 0
direction = ""
location = 0
friend1Location = 0
friend2Location = 0
friend3Location = 0
friendsFound = 0
friend1Found = False
friend2Found = False
friend3Found = False

locations = {
    1: "You've entered a mysterious forest!",
    2: "You've found yourself in a dark jungle!"
}




def move(location, direction):
    gameMap = {
        0: {
            "L": 1,
            "R": 2
        },
        1: {
            "L": 3,
            "R": 4
        }
    }
    global moves 
    moves = moves + 1
    global energy
    energy = energy - 1
    return gameMap[location][direction]




print("You've arrived on a deserted island! You must find your missing friends before your energy runs out!")

direction = input("Which direction do you want to go? L or R: ")

location = move(location, direction)
print(location)
