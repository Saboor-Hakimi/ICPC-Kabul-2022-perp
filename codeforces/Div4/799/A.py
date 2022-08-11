n = int(input())
for _ in range(n):
    a, b, c, d = list(map(int, input().split()))
    ppl = 0
    for person in [b,c,d]:
        if person > a:
            ppl += 1
    print(ppl)