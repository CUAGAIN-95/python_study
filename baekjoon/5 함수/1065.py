def check(a) :
    if (a < 100) :
        return 1
    a = str(a)
    d = int(a[1]) - int(a[0])
    for i in range(1, len(str(a))):
        if (d != int(a[i]) - int(a[i - 1])) :
            return 0
    return 1

n = int(input())
count = 0
for i in range(1, n + 1) :
    count += check(i)
print(count)