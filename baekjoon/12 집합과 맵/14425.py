import sys

N, M = map(int, sys.stdin.readline().split())
S = []
for i in range(N):
    S.append(sys.stdin.readline())
S = set(S)
count = 0
for i in range(M):
    word = sys.stdin.readline()
    if word in S:
        count += 1
print(count)