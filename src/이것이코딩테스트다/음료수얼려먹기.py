n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(r, c):
    global graph, visited
    visited[r][c] = True
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if nr >= 0 and nc >= 0 and nr < n and nc < m and visited[nr][nc] == False and graph[nr][nc] == 0:
            dfs(nr, nc)
count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 0:
            dfs(i,j)
            count += 1

print(count)
    

# 책정답
# n,m = map(int,input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# def dfs(x, y):
#     if x <=1 or x > n or y<=-1 or y >= m :
#         return False
    
#     if graph[x][y] == 0:
#         graph[x][y] = 1
        
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# result=0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1

# print(result)
