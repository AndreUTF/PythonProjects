LOW = 1
HIGH = 2047


# print("Please think of anumber between {} and {}"
#       .format(low, high))
# input("Please ENTER to start")


# guesses = 1
# while low != high:
#     print("\tGuessing in the range of {} to {}".format(low,high))
#     guess = low + (high - low) // 2
#     high_low = input("My guess is {}. Should I guess higher or lower?"
#                      "Enter h or l, or c if my guess was correct.".format(guess).casefold())
#     if high_low == "h":
#         # Guess higher. The low of the range becomes 1 greater than the guess.
#         low = guess + 1
#     elif high_low == "l":
#         high = guess - 1
#     elif high_low == "c":
#         print("I got it in {} guesses".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c")
#     guesses += 1
# else:
#     print("You thought of the number {}".format(low))
#     print("I got it in {} guesses".format(guesses))
def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range of {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower?"
        # "Enter h or l, or c if my guess was correct.".format(guess).casefold())
        # if high_low == "h":
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses
        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1
print("I guessed without being told {} times.Max {} guesses"
      .format(correct_count, max_guesses))


def fizz_buzz(number: int) -> str:
    """
    Play fizz buzz
    :param number: Enter the number of your play
    :return: 'Fizz' if the number is divided by 3,
        'Buzz' if the number is divided by 5,
        'Fizz-Buzz' if the number is divided by 3 and 5
    """
    turn_count = 0
    if number%3 == 0:
        return "fizz"
    elif number%5 == 0:
        return "buzz"
    elif number%3 == 0 and number%5 ==0:
        return "fizz-buzz"
    else:
        return str(number)


for i in range(1, 101):
    print(fizz_buzz(i))