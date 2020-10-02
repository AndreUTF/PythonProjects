import sys


number1 = int(input("Enter the first number: "))

number2 = int(input("Enter the second number: "))

try:
    print(number1/number2)
except ZeroDivisionError:
    print("You can not divide a by zero!!!!")
except OverflowError:
    print("You can not divide by a number so small")
except ValueError:
    print("The entries are wrong!!!!!!!")


def getInt(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(0)
        finally:
            print("The finally clause always execute")


first_number = getInt("Please enter first number")
second_number = getInt("Please enter second number")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can not divide by zero")