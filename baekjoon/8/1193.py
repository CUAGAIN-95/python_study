n = int(input())

i = 1
cnt = 1
while n > cnt:
    cnt = cnt + i + 1
    i += 1
if i % 2 == 0:
    x = i
    y = 1
    while n != cnt:
        x -= 1
        y += 1
        cnt -= 1
else:
    x = 1
    y = i
    while n != cnt:
        x += 1
        y -= 1
        cnt -= 1
print(x, '/', y, sep="")
