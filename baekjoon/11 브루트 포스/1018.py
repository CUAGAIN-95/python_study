import sys

M, N = map(int, sys.stdin.readline().split())

color = [""] * M
check = [[0] * N for _ in range(M)]

for i in range(M):
    color[i] = sys.stdin.readline()

first_color = color[0][0]

for i in range(M):
    for j in range(N):
        now_color = color[i][j]
        if (i + j) % 2 == 0:
            if first_color != color[i][j]:
                check[i][j] = 1
        else:
            if first_color == color[i][j]:
                check[i][j] = 1

min_check = -1
for i in range(M - 7):
    for j in range(N - 7):
        count_0 = 0
        count_1 = 0
        for x in range(8):
            for y in range(8):
                if check[i + x][j + y] == 1:
                    count_1 += 1
                else:
                    count_0 += 1
        if min_check == -1 or min_check > min(count_0, count_1):
            min_check = min(count_0, count_1)

print(min_check)
