T = int(input())

board = [[0] * 15 for _ in range(15)]
for j in range(0, 15):
    board[0][j] = j + 1
for i in range(1, 15):
    for j in range(0, 15):
        if j == 0:
            board[i][j] = 1
        else:
            board[i][j] = board[i - 1][j] + board[i][j - 1]
for i in range(0, T):
    k = int(input())
    n = int(input())
    print(board[k][n - 1])
