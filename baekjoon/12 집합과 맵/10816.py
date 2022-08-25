# import sys

# def lower_bound(nums, target):
#     left, right = 0, len(nums)

#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#     return right

# def upper_bound(nums, target):
#     left, right = 0, len(nums)

#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] <= target:
#             left = mid + 1
#         else:
#             right = mid
#     return right

# n = int(sys.stdin.readline())
# nl = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# ml = list(map(int, sys.stdin.readline().split()))

# nl.sort()
# for i in ml:
#     print(upper_bound(nl, i) - lower_bound(nl, i), end=' ')

###############

# import sys
# import bisect

# n = int(sys.stdin.readline())
# nl = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# ml = list(map(int, sys.stdin.readline().split()))
# nl.sort()
# for i in ml:
#     print(bisect.bisect_right(nl, i) - bisect.bisect_left(nl, i), end=' ')

import sys
from collections import Counter

n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ml = list(map(int, sys.stdin.readline().split()))
c = Counter(nl)

for i in ml:
    if i in c:
        print(c[i], end=' ')
    else:
        print(0, end=' ')
