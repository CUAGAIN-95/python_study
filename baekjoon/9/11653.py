def is_prime(num):
    if num < 2:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            return False
    return True


n = int(input())
i = 2
while i <= int(n ** 0.5) + 1:
    if n == 1:
        break
    if is_prime(n):
        print(n)
        break
    if n % i == 0:
        print(i)
        n = n // i
        i = 2
    elif i == 2:
        i += 1
    else:
        i += 2
