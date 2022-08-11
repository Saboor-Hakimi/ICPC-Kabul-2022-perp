n = int(input())
anton, danik = 0, 0

games = input()

for game in games:
    if game == "A":
        anton += 1
    elif game == "D":
        danik += 1
# print(anton, danik)
if anton == danik:
    print("Friendship")
elif anton > danik:
    print("Anton")
else:
    print("Danik")