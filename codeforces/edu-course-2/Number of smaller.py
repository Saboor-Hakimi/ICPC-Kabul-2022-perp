n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


res = []


for j in b:
    count = 0
    for i in a:
        if i < j:
            count += 1
    res.append(count)
        

    
print(*res)