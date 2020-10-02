def python_food():
    # print("spam and eggs")
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', end_char= '\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    # text = str(text)
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end_char, file=file, flush=flush)
    return " " * left_margin + text


# with open("centred", mode='w') as centred_file:

# call the function
# python_food()
# centre_text("spam and eggs")
# centre_text("spam, spam and eggs")
# centre_text("12")
# centre_text("spam, spam, spam and eggs")
# centre_text("first", "second", 3, 4, "spam", sep=':')

# s1 = centre_text("spam and eggs")
# print(s1)
# s2 = centre_text("spam, spam and eggs")
# print(s2)
# s3 = centre_text("12")
# print(s3)
# s4 = centre_text("spam, spam, spam and eggs")
# print(s4)
# s5 = centre_text("first", "second", 3, 4, "spam", sep=':')
# print(s5)
with open("menu", "w") as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file = menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file = menu)
    s3 = centre_text("12")
    print(s3, file = menu)
    s4 = centre_text("spam, spam, spam and eggs")
    print(s4, file = menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=':')
    print(s5, file = menu)

