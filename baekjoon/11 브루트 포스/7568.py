n = int(input())

arr = [[]] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))
rank = [1] * n
for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i] += 1
for i in rank:
    print(i, end=' ')
