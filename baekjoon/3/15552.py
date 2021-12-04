# import란 c에서 include를 뜻한다
# input과 sys.stdin.readline 둘 다 데이터를 받을 때 사용하며
# sys.stdin.readline이 빠르다

import sys
T = int(input())

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)