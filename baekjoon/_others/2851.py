arr = [0] * 10
for i in range(10):
    arr[i] = int(input())

sum_nums = 0
previous_sum = sum_nums
for i in arr:
    previous_sum = sum_nums
    sum_nums += i
    if sum_nums >= 100:
        break

if abs(100 - previous_sum) < abs(sum_nums - 100):
    print(previous_sum)
else:
    print(sum_nums)
