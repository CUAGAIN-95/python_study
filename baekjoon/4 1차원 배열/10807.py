import sys

a = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())

print(arr.count(t))