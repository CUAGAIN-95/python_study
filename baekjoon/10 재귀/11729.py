def hanoi(n, from_pos, aux_pos, to_pos):
    # 한 개만 있으면 목적기둥으로 이동
    if n == 1:
        print(from_pos, to_pos)
        return
    # 큰 원판 빼고 나머지 원판 보조 기둥으로 이동
    hanoi(n - 1, from_pos, to_pos, aux_pos)
    # 큰 원판 목적지로 이동
    print(from_pos, to_pos)
    # 보조 기둥에서 목적 기둥으로 이동
    hanoi(n - 1, aux_pos, from_pos, to_pos)


n = int(input())

print(2 ** n - 1)
hanoi(n, 1, 2, 3)
