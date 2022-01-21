import sys
from collections import Counter


def my_round(x, y):
    if x >= 0:
        return int(x / y + 0.5)
    else:
        return int(x / y - 0.5)


n = int(sys.stdin.readline())
nums = [0] * n

for i in range(n):
    nums[i] = int(sys.stdin.readline())

print(my_round(sum(nums), n))
nums.sort()
print(nums[n // 2])
count = Counter(nums).most_common(2)
if len(nums) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
print(max[nums] - min(nums))
