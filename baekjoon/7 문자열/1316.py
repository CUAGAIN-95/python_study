n = int(input())
count = 0

for i in range(n):
    word = input()
    group = set()
    last_chr = 0
    for j in word:
        if j not in group:
            group.add(j)
            last_chr = j
        elif j in group and last_chr == j:
            continue
        else:
            group.add(-1)
            break
    if -1 not in group:
        count += 1
print(count)
