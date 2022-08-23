import sys

N, M = map(int, sys.stdin.readline().split())

S = {}
for i in range(1, N + 1):
    S[i] = sys.stdin.readline().rstrip()

R = dict(map(reversed, S.items()))
for j in range(M):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        print(S[int(q)])
    else:
        print(R[q])