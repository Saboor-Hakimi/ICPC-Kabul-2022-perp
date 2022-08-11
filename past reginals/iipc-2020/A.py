n = int(input())
k = int(input())
p = int(input())
q = int(input())

a, b = n-k, p-q
if a>b:
    print("Shekarestan")
elif b>a:
    print("Namakestan")
else:
    print("Equal")