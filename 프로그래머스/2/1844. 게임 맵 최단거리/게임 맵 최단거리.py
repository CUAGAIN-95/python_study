from collections import deque

def solution(maps):
    shortest_dist = -1
    row_len = len(maps)
    col_len = len(maps[0])
    if maps[0][0] == 0 and maps[row_len -1][col_len - 1] == 0:
        return shortest_dist
    
    visited = [[False] * col_len for _ in range(row_len)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    while queue:
        cur_r, cur_c, cur_dist = queue.popleft()
        if cur_r == row_len - 1 and cur_c == col_len - 1:
            shortest_dist = cur_dist
            break
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if maps[next_r][next_c] == 1:
                    if not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_dist + 1))
                        visited[next_r][next_c] = True
    answer = shortest_dist
    return answer
    