
user_input = "-";
while user_input != "0":
    if user_input in "12345":
        print("you choose {}.".format(user_input))
    else:
        print("Please choose your option from the list below:")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo swimming")
        print("4.\tHave Dinner")
        print("5.\tGo to bed")
        print("0.\t Exit")
    user_input = input()