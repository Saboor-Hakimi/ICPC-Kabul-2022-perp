n = str(input())

len4, len7 = 0,0

for i in n:
    if i != '4' and i != '7':
        print('NO')
        exit()
for i in n:
    if i=='4':
        len4 += 1
    elif i=='7':
        len7+=1
if (len4+len7==7) or (len4+len7==4):
    print("NO")
    exit()
print("NO")