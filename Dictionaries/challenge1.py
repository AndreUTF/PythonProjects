# locations = {0: "You are sitting in front of computer learning python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }
exits = {0: {"Q": 0},
         1: {"W": 2, "2": 2, "E": 3, "3": 3, "N": 5, "5": 5, "S": 4, "4": 4, "Q": 0},
         2: {"N": 5, "5": 5, "Q": 0},
         3: {"W": 1, "1": 1, "Q": 0},
         4: {"N": 1, "1": 1, "W": 2, "2": 2,"Q": 0},
         5: {"W": 2, "2": 2, "S": 1, "1": 1,"Q": 0}}
namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1} }
vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}
# print(locations[1].keys())
# print(locations[1]["desc"])
# print(locations[1]["exits"])
# print(locations[1]["namedExits"].keys())

loc = 1
while True:  # loops while input is different from 0
    availableExits = ", ".join(locations[loc]["exits"].keys())  # creates am empty string

    # print(locations[loc])  # print location from dictionary
    print(locations[loc]["desc"])  # print location from dictionary

    if loc == 0:
        break
    else:
        # allExits = exits[loc]["exits"].copy()
        # allExits.update(namedExits[loc])
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])
        # print(allExits)
        # allExits.update(locations[loc]["namedExits"])
        print(allExits)

    direction = input("Available exists are " + availableExits).upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You can go in the direction")


# while True:  # loops while input is different from 0
#     availableExits = ", ".join(locations[loc].keys())  # creates am empty string
#
#     print(locations[loc])  # print location from dictionary
#
#     if loc == 0:
#         break
#     else:
#         allExits = exits[loc].copy()
#         allExits.update(namedExits[loc])
#
#     direction = input("Available exists are " + availableExits).upper()
#     print()
#     if len(direction) > 1:
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:
#                 direction = vocabulary[word]
#                 break
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You can go in the direction")
#
# print(locations.values())

# while True:  # loops while input is different from 0
#     availableExits = ""  # creates am empty string
#     for direction in exits[loc].keys():  # for loop that runs throughout
#         availableExits += direction + ", "
#
#     print(locations[loc])  # print location from dictionary
#
#     if loc == 0:  # if input loc is equals to 0
#         break  # breaks from loop
#     direction = input("Available exists are " + availableExits.upper())
#     print()
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You can go in yhe direction")