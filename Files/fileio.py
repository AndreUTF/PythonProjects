# jabber = open("C:\sample.txt",'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end = '')
# jabber.close()

# with open("C:\sample.txt") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("C:\sample.txt") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end = '')
#         line = jabber.readline()

with open("C:\sample.txt") as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end ='')