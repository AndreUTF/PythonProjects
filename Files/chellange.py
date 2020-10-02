# with open("sample.txt", 'w') as sample_txt:
#     contents = imelda_file.readline()
number = 2
with open("sample.txt", 'w') as sample_text:
    for i in range(1, 13, 1):
        for j in range(1, 13, 1):
            print("{0:>3d} times {1: 3d} is {2:>3d}".format(j, i, i * j),
                  file=sample_text)
        print("-" * 40, file=sample_text)

# number = 2
# for i in range(1, 13, 1):
#     print("{0} times {1} is {2}".format(i, number, i * number))
# print("-" * 40)
