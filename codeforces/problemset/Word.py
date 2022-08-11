
word = input()

lower, upper = 0, 0
for char in word:
    if char.islower():
        lower += 1
    else:
        upper += 1
# print(lower, upper)
if lower == upper:
    print(word.lower())
elif lower > upper:
    print(word.lower())
else:
    print(word.upper())