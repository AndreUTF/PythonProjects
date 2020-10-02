age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
#     print("Have a good day at work")

# if 16 <= age <= 65:
#     print("Have a good day at work")
if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy free time")

print("-" * 80)

if 16 < age > 65:
    print("Enjoy free time")
else:
    print("Have a good day at work")

for i in range(100):
    if i%7 == 0:
        print(i)