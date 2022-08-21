def d(n) :
    ret = n
    for i in range(len(str(n))) :
        ret += int(str(n)[i])
    return ret

a = set()
for i in range(10000) :
    a.add(i + 1)
for i in range(10000) :
    if (d(i + 1) <= 10000):
        a.discard(d(i + 1))
a = list(a)
for i in range(len(a)) :
    print(a[i])