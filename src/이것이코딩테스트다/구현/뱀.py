n = int(input())
k = int(input())

board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    board[a][b] = 1

info = []

l = int(input())

for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

def turn(direction,c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction

def simulate():
    x, y =1,1
    board[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] !=2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time
                

print(simulate())