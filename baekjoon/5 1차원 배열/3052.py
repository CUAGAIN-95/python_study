# arr = []
# for i in range(10):
#     arr.append(int(input()))
# count = [0] * 42
# for i in range(10):
#     count[arr[i] % 42] = 1
# print(count.count(1))

count = set()
for _ in range(10):
    count.add(int(input()) % 42)
print(count.__len__())