n = int(input())
arr = list(map(int, input().split()))

m = max(arr)
score = [0] * n
for i in range(n):
    score[i] = arr[i] / m * 100
print(sum(score) / n)