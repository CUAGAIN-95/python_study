A, B, V = map(int, input().split())
day = (V - A) / (A - B)

if (V - A) % (A - B) == 0:
    day = day + 1
else:
    day = day + 2
print(int(day))
# print(amth.ceil(day) + 1)