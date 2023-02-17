from collections import deque

def turn(a, d):
    if a == 'D':
        d = (d+1) % 4
    else:
        d = (d-1) % 4
    return d

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    
l = int(input())

d_info = deque()

for _ in range(l):
    a,b = input().split()
    d_info.append((int(a),b))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

d = 0

x,y = 0,0

time = 0

index = 0

graph[0][0] = 2

q = [(x,y)]

while True:
        
    nx = x + dx[d]
    ny = y + dy[d]
    
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 2:
    
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            q.append((nx,ny))
            px, py = q.pop(0)
            graph[px][py] = 0

        if graph[nx][ny] == 1:
            graph[nx][ny] = 2
            q.append((nx,ny))
    
    else:
        time += 1
        break
    
    x, y = nx, ny
    
    time += 1
    
    if index < l and time == d_info[index][0]:
        d = turn(d_info[index][1], d)
        index += 1

print(time)

