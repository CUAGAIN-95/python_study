n = input()

num = int(n)
ret = 0
for i in range(max(num - (len(n) * 9), 0), num):
    sum_num = i
    for j in str(i):
        sum_num += int(j)
    if sum_num == num:
        ret = i
        break
print(ret)
