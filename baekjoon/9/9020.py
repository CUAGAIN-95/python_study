n = int(input())

for _ in range(n):
    num = int(input())

    a = b = int(num / 2)
    a -= 1
    b += 1
    print(a, b)
