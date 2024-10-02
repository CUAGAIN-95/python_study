from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)
    
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

def solution(n, computers):
    graph = {}
    for i in range(n):
        graph[i] = []
        for j in range(n):
            node = computers[i][j]
            if i != j and node == 1:
                graph[i].append(j)
    network = []
    for i in range(n):
        net = set(bfs(graph, i))
        if net not in network:
            network.append(net)
    
    answer = len(network)
    return answer
