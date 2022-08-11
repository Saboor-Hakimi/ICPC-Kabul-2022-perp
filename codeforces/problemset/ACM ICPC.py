scores = list(map(int, input().split()))

for a in range(len(scores)):
    for b in range(len(scores)):
        for c in range(len(scores)):
            for d in range(len(scores)):
                for e in range(len(scores)):
                    for f in range(len(scores)):
                        if a not in [b,c,d,e,f] and b not in [a,c,d,e,f] and c not in [a,b,d,e,f] and d not in [a,b,c,e,f] and e not in [a,b,c,d,f] and f not in [a,b,c,d,e]:
                            if scores[a] + scores[b] + scores[c] == scores[d] + scores[e] + scores[f]:
                                print("YES")
                                exit()
print("NO")