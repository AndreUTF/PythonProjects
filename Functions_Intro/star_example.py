numbers = (0, 1, 2, 3, 4, 5) # print a tuple for numbers in 0 to 5

print(numbers) # print as a tuple with parenthesis
print(*numbers, sep = ";")# print number in tuple with separator


def test_star(*args): # print value of args
    print(args) # print a list of values from a tuple
    for x in (args): # for loop to print values
        print(x) # print values


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()