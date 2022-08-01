n, m = list(map(int, input().split()))
arr0 = list(map(int, input().split()))
arr1 = list(map(int, input().split()))

arr0.append(99999999999999)
arr1.append(99999999999999)


# print(arr0, arr1)

i, j, k = 0, 0, 0
res = []


while i < len(arr0) or j < len(arr1):
    if (i==len(arr0)-1) and (j==len(arr1)-1):
        break
    # print(i, j)
    # print(res)
    # if j==len(arr1) or (i < len(arr0) and arr0[i] < arr1[j]):
    #     res.append(arr0[i])
    #     i+=1
    #     k+=1
    if arr0[i] < arr1[j]:
        res.append(arr0[i])
        i+=1
        k+=1
    else:
        res.append(arr1[j])
        j+=1
        k+=1
    

print(*res)