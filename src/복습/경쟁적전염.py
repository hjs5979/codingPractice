from collections import deque

n,k = map(int,input().split())

graph = []

data = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()

# n,k = 3,3

# graph = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]

# s,x,y = 2,3,2

q = deque(data)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

# for number in range(1,k+1):
#     for i in range(n):
#             for j in range(n):
#                 if graph[i][j] == number:
#                     q.append((i,j))

while q:

    num, time, tempx, tempy = q.popleft()
    
    if s == time:
        break

    for i in range(4):
        nx = tempx + dx[i]
        ny = tempy + dy[i]
    
        if nx < 0 or nx >=n or ny <0 or ny >= n:
            continue
        
        if graph[nx][ny] == 0:
            graph[nx][ny] = num
            q.append((num, time+1, nx,ny))

print(graph[x-1][y-1])

#     if num > k:
#         num = 1
#         time += 1
    
#     if time == s:
#         print(graph[x-1][y-1])
#         print(graph)
#         break

    
    




