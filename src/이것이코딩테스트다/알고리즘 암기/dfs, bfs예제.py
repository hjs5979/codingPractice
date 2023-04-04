
# graph : 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# 1번 인덱스 => 1번과 연결된 노드 리스트

graph =[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# visited : 노드 수만큼(0포함) False 리스트
visited = [False] * 9

# ----------------------------------------------------------------------
# dfs : 경로의 특징을 저장해둬야 하는 문제
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
            
dfs(graph, 1, visited)

# ----------------------------------------------------------------------
# bfs : 최단경로
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
