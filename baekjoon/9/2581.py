def is_prime(num):
    if num < 2:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            return False
    return True


M = int(input())
N = int(input())

min_prime = 0
sum_prime = 0
for i in range(M, N + 1):
    if not is_prime(i):
        continue
    if min_prime == 0:
        min_prime = i
    sum_prime += i
if min_prime == 0:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)
