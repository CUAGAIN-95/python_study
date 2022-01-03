s = input()

for i in range(0, 26):
    print(s.find(chr(i + ord('a'))), end=' ')