import sys
n = int(input())

for i in range(n):
    score = list(map(int, sys.stdin.readline().split()))
    average = sum(score[1:]) / score[0]
    count = 0
    for i in range(score[0]):
        if (score[i + 1] > average):
            count += 1
    print('{0:.3f}%'.format(count / score[0] * 100))
