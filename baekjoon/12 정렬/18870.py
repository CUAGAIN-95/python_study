import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sort_arr = list(sorted(set(arr)))
dic = {value: index for index, value in enumerate(sort_arr)}
for i in arr:
    print(dic[i], end=' ')
