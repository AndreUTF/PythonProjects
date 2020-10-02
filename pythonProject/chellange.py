name = input("What's your name? ")

age = int(input("What's your age? "))

if 18 <= age < 31:
    print("Welcome to the holiday, {}!".format(name))
    print("Welcome club 18-30, {}!".format(name))
else:
    print("You aren't welcome to the holiday, {}!,"
         "you must have between 18 an 30".format(name))