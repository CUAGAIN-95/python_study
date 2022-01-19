import sys


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
print(nums[int((n - 1) / 2)])

count = 1


range_num = nums[n - 1] - nums[0]

print(range_num)