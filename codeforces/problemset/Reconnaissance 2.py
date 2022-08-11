n = int(input())
data = list(map(int, input().split()))

intial_diff = 99999999999999999999999999
solders = [1, 2]

for i in range(len(data)):
    for j in range(len(data)):
        if i != j  and abs(data[i] - data[j]) < intial_diff and (abs(i-j) == 1 or (i==0 and j==len(data)-1) or (i==len(data)-1 and j==0)):
            # print(data[i], data[j], i, j, abs(data[i] - data[j]), intial_diff)
            intial_diff = abs(data[i] - data[j])
            solders = [i+1, j+1]
print(*solders)