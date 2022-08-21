import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    arr.append(xy)
arr.sort()
for x, y in arr:
    print(x, y)
