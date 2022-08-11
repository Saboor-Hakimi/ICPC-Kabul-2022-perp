n = int(input())
for _ in range(n):
    m = int(input())
    data = list(map(int, input().split()))
    flag1, flag2 = False, False
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i != j and i != k and j != k:
                    if str(data[i] + data[j] + data[k])[-1] == '3':
                        print("YES")
                        # print(i, j, k)
                        flag1, flag2 = True, True
                        break
            if flag2:
                break
        if flag1:
            break
    if not flag1:
        print("NO")
                        
    