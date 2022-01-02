n = int(input())

prime = [True] * (10000 + 1)
for i in range(2, int(10000 ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, 10000 + 1, i):
            prime[j] = False

for _ in range(n):
    num = int(input())

    a = b = int(num / 2)
    while True:
        if prime[a] and prime[b] and a + b == num:
            print(a, b)
            break
        a -= 1
        b += 1
