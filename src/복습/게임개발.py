n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

# n, m = 4, 5
# x, y, d = 1, 1, 0

# graph = [[1, 1, 1, 1, 1],
#          [1, 0, 1, 1, 1],
#          [1, 0, 0, 0, 1], 
#          [1, 1, 1, 1, 1]]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d):
    d -= 1
    if d < 0:
        d=3
    return d

graph[x][y] = -1

move_cnt = 1
turn_cnt = 0

while True:
    d = turn(d)
    turn_cnt += 1
    nx = x + dx[d]
    ny = y + dy[d]
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = -1
        x, y = nx, ny
        move_cnt += 1
        turn_cnt = 0
        continue
    
    if turn_cnt == 4:
        
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == -1:
            x, y = nx, ny
            turn_cnt = 0
            
        else:
            break   

print(move_cnt)