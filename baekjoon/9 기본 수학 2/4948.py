import sys

nums = []
while True:
    i = int(sys.stdin.readline())
    if i == 0:
        break
    nums.append(i)

max_num = max(nums)
m2 = max_num * 2
prime = [True] * (m2 + 1)
for i in range(2, int(m2 ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, m2 + 1, i):
            prime[j] = False

for i in nums:
    print(prime[i + 1:i * 2 + 1].count(True))
