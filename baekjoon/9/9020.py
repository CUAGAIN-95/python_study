n = int(input())

for _ in range(n):
    num = int(input())

    a = b = int(num / 2)
    while a > 1:
        a -= 1
    while b < num:
        b += 1
    print(a, b)
