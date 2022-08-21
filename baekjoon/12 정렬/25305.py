import sys

N, k = sys.stdin.readline().split()
x = list(map(int, sys.stdin.readline().split()))

x.sort(reverse=True)
print(x[int(k)-1])