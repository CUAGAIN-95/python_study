import sys

count = [0, 0, 0, 0, 0, 0]

dice = list(map(int, sys.stdin.readline().split()))

for i in dice:
    count[i - 1] += 1

max = 0
ind = 0
for i in range(6):
    if count[i] >= max:
        max = count[i]
        ind = i + 1

if max == 3:
    print(10000 + ind * 1000)
elif max == 2:
    print(1000 + ind * 100)
else:
    print(ind * 100)