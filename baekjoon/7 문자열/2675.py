n = int(input())

for i in range(n):
    r, word = input().split()
    for j in word:
        print(j * int(r), end='')
    # for j in range(len(word)):
    #     print(word[j] * int(r), end='')
    print()