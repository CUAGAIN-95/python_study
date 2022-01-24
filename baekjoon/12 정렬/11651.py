import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    arr.append(xy)
arr.sort(key=lambda a: (a[1], a[0]))
for x, y in arr:
    print(x, y)
