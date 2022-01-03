import math

T = int(input())

for i in range(0, T):
    H, W, N = map(int, input().split())
    x = math.ceil(N / H)
    y = N % H
    if y == 0:
        y = H
    print(y * 100 + x)
