n = int(input())
for _ in range(n):
    board = []
    input()
    posX, posY = 0, 0
    for i in range(8):
        
        board.append(list(input()))
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                if board[i][j] == '#' and board[i-1][j-1] == '#' and board[i-1][j+1] == "#" and board[i+1][j-1] == "#" and board[i+1][j+1] == "#":
                    posX, posY = i+1, j+1
                    break
            except:
                pass
    print(posX, posY)
    # print(board)
    