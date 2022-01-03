def triangle(num):
    return (num * (num + 1)) / 2


n = int(input())

i = 0
while n > 6 * triangle(i) + 1:
    i += 1
print(i + 1)
