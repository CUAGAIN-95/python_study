import math

# n = int(input())

# for i in range(n):
a, b = map(int, input().split())
d = b - a
max_move = math.sqrt(d)
print(math.sqrt(d), math.ceil(max_move), math.floor(max_move))
