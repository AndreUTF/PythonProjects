# myList = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "123456789"
# newString = ''
# # for c in myList: Using a for loop
# #     myString += c + ", "
# # print(newString)
#
# newString = ", ".join(letters)
# print(newString)
#
# newString1 = ''
#
# newString1 = " mississippi ".join(numbers)
# print(newString1)

locations = {0: "You are sitting in front of computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 0, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
loc = 1
while True:  # loops while input is different from 0
    availableExits = ""  # creates am empty string
    for direction in exits[loc].keys():  # for loop that runs throughout
        availableExits += direction + ", "

    print(locations[loc])  # print location from dictionary

    if loc == 0:  # if input loc is equals to 0
        break  # breaks from loop
    direction = input("Available exists are " + availableExits.upper())
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You can go in yhe direction")
