n, m = map(int,input().split())
x, y, d = map(int,input().split())

mp = []

l = [[0] * m for _ in range(n)]

l[x][y] =1

for _ in range(n):
    mp.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global d
    d -=1
    if d == -1:
        d = 3

count = 1

turn_time = 0

while True:
    turn_left()

    nx = x + dx[d]
    ny = y + dy[d]

    if (l[nx][ny] == 0) and (mp[nx][ny] == 0):
        l[nx][ny] = 1
        x,y = nx,ny
        count +=1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4 :
        nx = x-dx[d]
        ny = y-dy[d]

        if mp[nx][y] == 0:
            x,y = nx, ny
        
        else:
            break

        turn_time = 0

print(count)
        

    


