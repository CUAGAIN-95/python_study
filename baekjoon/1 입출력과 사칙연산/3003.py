import sys

arr = list(map(int, sys.stdin.readline().split()))
base = [1, 1, 2, 2, 2, 8]
for i in range(6) :
    print(base[i] - arr[i], end=" ")