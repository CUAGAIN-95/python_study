import math
import sys
A, B, C = map(int, sys.stdin.readline().split())

try:
    n = A / (B - C)

except ZeroDivisionError:
    print(-1)