import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

for i in range(N):
    a, b = sys.stdin.readline().split()
    X -= int(a) * int(b)

if X == 0:
    print("Yes")
else:
    print("No")