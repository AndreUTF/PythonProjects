numbers =  [1, 45 , 33, 12, 60]
number = 0;
for number in numbers:
    if number%8 == 0:
        # rejected the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")