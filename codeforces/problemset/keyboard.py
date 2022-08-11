n = int(input())

for _ in range(n):
    board = input()
    word = input()
    numb = []
    for char in word:
        for num, chary in enumerate(board):
            if chary == char:
                numb.append(num)
                break
    # print(numb)
    res = 0
    for i in range(len(numb)-1):
        res += abs(numb[i+1] - numb[i])
    print(res)