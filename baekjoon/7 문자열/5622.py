word = input()
# x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for i in word:
    for j in arr:
        if j.find(i) != -1:
            time += arr.index(j) + 3

print(time)
