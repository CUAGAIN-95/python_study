import sys

word = sys.stdin.readline()
num = [0] * (len(word) - 1)

for i in range(len(word) - 1):
    num[i] = int(word[i])
num.sort(reverse=True)
for i in num:
    print(i, end='')
