n, m = map(int,input().split())
x, y, d = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

loc = [[0] * m for _ in range(n)]

loc[x][y] == 1

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def direction_move():
    global d
    d -= 1
    if d == -1:
        d == 3

answer = 0

while True:
    turn_cnt = 0
    for _ in range(4):
        direction_move()
        
        nx , ny = x+dx[d], y+dy[d]
        if  0 <= nx < m and 0<= ny < n and loc[nx][ny] != 1 and graph[nx][ny] != 1:
            x, y = nx, ny
            answer += 1
            
        # turn_cnt += 1
    nx, ny = -x, -y
    if 0 <= nx < m and 0<= ny < n and graph[nx][ny] != 1:
        x, y = -x, -y
    else:
        break
print(answer)
    
            

        
        