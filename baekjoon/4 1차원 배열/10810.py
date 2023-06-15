import sys

n, m = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for target in range(i - 1, j):
        arr[target] = k

print(*arr)