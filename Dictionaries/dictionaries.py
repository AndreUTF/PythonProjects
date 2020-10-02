fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# print(fruit)
# fruit.clear()
# print(fruit)
# fruit["tomato"] = "a red fruit that fits with a salad"

print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key, "We don't have a +" + dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)


# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 40)
#
# ordered_key = list(fruit.keys())
# ordered_key.sort()
# for f in ordered_key:
#     print(f + " - " + fruit[f])
#
# print()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " -> " + fruit[f])
#
# print()
# for key in fruit:
#     print(fruit[key])
#
# print()
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# print()
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
#
# print(fruit.items())

# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
