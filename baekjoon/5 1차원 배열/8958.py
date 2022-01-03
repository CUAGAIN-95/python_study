n = int(input())

for _ in range(n):
    arr = input()
    count = [0] * len(arr)
    flag = 0
    for i in range(len(arr)):
        if (arr[i] == 'O'):
            count[i] = flag + 1
            flag += 1
        else:
            flag = 0
    print(sum(count))