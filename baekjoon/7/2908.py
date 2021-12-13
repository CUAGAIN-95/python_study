# a, b = input().split()
#
# a = int(a[2] + a[1] + a[0])
# b = int(b[2] + b[1] + b[0])
# if a > b:
#     print(a)
# else:
#     print(b)

# 다른 방식의 풀이법
a, b = input().split()

a = a[::-1]
b = b[::-1]

print(max(a, b))
