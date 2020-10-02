sampleText = "Python is a powerful lnaguage"
print(sampleText)
vowels = frozenset("aeiou")
print(vowels)
# vowels = {"a", "e", "i", "o", "u"}
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)