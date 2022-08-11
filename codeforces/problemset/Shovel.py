shovel_price, change = list(map(int, input().split()))



for i in range(1, 10001):
    temp = i * shovel_price
    # print(temp, temp % 10 , temp % 10 == chacnge)
    if temp % 10 == 0 or temp % 10 == change:
        print(i)
        exit()