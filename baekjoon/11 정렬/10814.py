import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    arr.append([age, name])
arr.sort(key=lambda x: (x[0]))
for i, j in arr:
    print(i, j)
