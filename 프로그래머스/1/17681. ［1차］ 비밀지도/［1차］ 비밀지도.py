def d_to_b(num, n):
    result = []
    i = num
    while True:
        i = num // 2
        s = num % 2
        result.append(s)
        num = i
        if i == 0:
            break
    for _ in range(n - len(result)):
        result.append(0)
    result.reverse()
    return result

def to_hash(arr):
    s = ''
    for i in arr:
        if i == 1:
            s += '#'
        else:
            s += ' '

    return s
    
def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        answer.append(a | b)

    for i in range(len(answer)):
        answer[i] = d_to_b(answer[i], n)
        answer[i] = to_hash(answer[i])
    return answer
