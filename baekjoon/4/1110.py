n = int(input())

i = n
count = 0

while True:
    q = i // 10
    r = i % 10
    new = q + r
    i = (r * 10) + (new % 10)
    count += 1
    if (i == n):
        break
print(count)