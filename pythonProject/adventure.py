available_exits = ["north","south","east","west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please chose a direction: ")
    if chosen_exit == "quit":
        print("Game over")
        break
else:
    print("aren't you glad that you got out")