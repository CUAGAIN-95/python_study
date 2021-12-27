import math

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    d = b - a
    max_move = math.sqrt(d)
    if max_move == math.ceil(max_move):
        print(int(max_move * 2 - 1))
    elif d <= math.ceil(max_move) * math.floor(max_move):
        print(math.floor(max_move) * 2)
    else:
        print(math.floor(max_move) * 2 + 1)
