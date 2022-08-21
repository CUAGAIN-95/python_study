n = int(input())

nums = list(map(int, input().split()))
arr = []
for i in nums:
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                arr.append(i)
            break
print(len(arr))
