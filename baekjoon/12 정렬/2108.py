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
max_count = 0
min2 = 0
mode_num = 0
for i in range(n):
    count = 1
    for j in range(i + 1, n):
        if nums[i] == nums[j]:
            count += 1
        else:
            break
    if max_count < count:
        mode_num = nums[i]
        max_count = count
        min2 = 0
    elif max_count == count:
        if min2 == 0:
            min2 = 1
            mode_num = nums[i]
    i += count
print(mode_num)
range_num = nums[n - 1] - nums[0]
print(range_num)
