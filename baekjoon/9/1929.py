def is_prime(num):
    if num < 2:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            return False
    return True


M, N = map(int, input().split())

nums = list(map(int, range(M, N + 1)))

print(nums)
for i in nums:
    if not is_prime(i):
        continue
    print(i)
