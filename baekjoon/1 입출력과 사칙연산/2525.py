import sys

A, B =  map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

if B + C < 60 :
    print(A, B + C)
else:
    D = (B + C) // 60
    E = (B + C) % 60
    if A + D < 24:
        print(A + D, E)
    else:
        print(A + D - 24, E)
