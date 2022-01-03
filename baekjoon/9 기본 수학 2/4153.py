while True:
    lines = list(map(int, input().split()))
    if lines[0] == 0:
        break
    lines.sort()
    if lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2:
        print("right")
    else:
        print("wrong")
