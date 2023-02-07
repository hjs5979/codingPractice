from collections import deque

# n,m = map(int,input().split())

# graph = []

# for _ in range(n):
#     graph.append(list(map(int,input())))

n,m = 5, 6

graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

start = (0,0)
q = deque()
q.append(start)

dx = [-1,0,0,1]
dy = [0,-1,1,0]

while q:
    tx, ty = q.popleft()
    
    for i in range(4):
        nx = tx + dx[i]
        ny = ty + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        if graph[nx][ny] == 0:
            continue
        
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[tx][ty] + 1
            q.append((nx,ny))


# print(graph)
print(graph[n-1][m-1])