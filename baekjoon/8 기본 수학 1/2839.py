n = int(input())

i = n // 5
if n % 5 == 0:
    print(i)
    exit()
x3 = 0
for x5 in range(i, -1, -1):
    if (n - (5 * x5)) % 3 == 0:
        x3 = (n - (5 * x5)) // 3
        break
if x3 == 0:
    print(-1)
else:
    print(x5 + x3)
