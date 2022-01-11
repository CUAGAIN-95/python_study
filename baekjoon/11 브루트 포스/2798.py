N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
sum_max = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if sum_max < arr[i] + arr[j] + arr[k] <= M:
                sum_max = arr[i] + arr[j] + arr[k]
print(sum_max)
