# import sys

# N = int(sys.stdin.readline())
# base = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# test = list(map(int, sys.stdin.readline().split()))

# base.sort()

# for i in test:
#     left = 0
#     right = N - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if base[mid] == i:
#             print(1, end=' ')
#             break
#         elif base[mid] > i:
#             right = mid - 1
#         else:
#             left = mid + 1
#     if base[mid] != i:
#         print(0, end=' ')

# in으로 대상을 찾을 때는 set이 list보다 빠르다.
import sys

N = int(sys.stdin.readline())
base = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))

h = []

for i in test:
    if i in base:
        h.append(1)
    else:
        h.append(0)
for i in h:
    print(i, end=' ')