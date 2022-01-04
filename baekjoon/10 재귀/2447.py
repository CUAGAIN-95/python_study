def star(num: int, x: list) -> list:
    out = []
    if num == 3:
        return x
    else:
        for i in x:
            out.append(i * 3)
        for i in x:
            out.append(i + ' ' * len(x) + i)
        for i in x:
            out.append(i * 3)
        return star(num // 3, out)


n = int(input())

first = ["***", "* *", "***"]
for j in star(n, first):
    print(j)
