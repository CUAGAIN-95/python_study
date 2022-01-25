import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    arr.append(word)
arr = list(set(arr))
arr.sort(key=lambda a: (len(a), a))
for i in arr:
    print(i)
