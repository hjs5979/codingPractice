
# graph : 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# 1번 인덱스 => 1번과 연결된 노드 리스트
graph =[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# visited : 노드 수만큼(0포함) False 리스트
visited = [False] * 9

def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:

            dfs(graph, i, visited)

#함수 호출
dfs(graph, 1, visited)


# start : 노드번호

from collections import deque

def bfs(graph, start, visited):
    # 큐에 시작 지점 삽입
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기(왼쪽에서 부터)
        v = queue.popleft()
        print(v, end= ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 함수호출
bfs(graph, 1, visited)


