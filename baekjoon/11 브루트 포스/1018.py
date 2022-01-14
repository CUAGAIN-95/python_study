import sys

M, N = map(int, sys.stdin.readline().split())

color = [""] * N
check = [[0] * N for _ in range(M)]

for i in range(M):
    color[i] = sys.stdin.readline()

main_color = color[0][0]
if main_color == 'B':
    other_color = 'W'
else:
    other_color = 'B'

for i in range(M):
    for j in range(N):
        now_color = color[i][j]
        if (i + j) % 2 == 0:
            if main_color != color[i][j]:
                check[i][j] = 1
        else:
            if other_color != color[i][j]:
                check[i][j] = 1

min_check = -1
for i in range(M - 7):
    for j in range(N - 7):
        count = 0
        for x in range(8):
            for y in range(8):
                if check[i + x][j + y] == 1:
                    count += 1
        if min_check == -1 or min_check > count:
            min_check = count



print(min_check)
