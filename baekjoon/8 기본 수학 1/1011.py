n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    d = b - a
    max_move = int(d ** 0.5)
    if max_move == d ** 0.5:
        print(max_move * 2 - 1)
    elif d <= max_move * (max_move + 1):
        print(max_move * 2)
    else:
        print(max_move * 2 + 1)
