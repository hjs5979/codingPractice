from collections import deque

def bfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    q = deque()
    q.append((x,y))
    array[x][y] = 1
    while q:
        tx, ty = q.popleft()
        
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            
            if 0 <= nx < n and 0<= ny < m:
                # print(nx,ny)
                # print(array)
                if array[nx][ny] == 0:
                    array[nx][ny] = 1
                    q.append((nx,ny))

n,m = map(int,input().split())

array = []

for _ in range(n):
    array.append(list(map(int,input())))

# print(array)

cnt = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            cnt += 1
            bfs(i,j)

print(cnt)