# a = int(input())
# b = int(input())
# print(a * (b % 10))
# print(a * int((b % 100) / 10))
# print(a * int(b / 100))
# print(a * b)

# 너무 깔끔한 코드

a = int(input())
b = input()
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))