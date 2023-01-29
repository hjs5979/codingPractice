socket = []

n,m = map(int,input().split())

for _ in range(n):
    socket.append(list(map(int,input())))

def fill(r,c):
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    
    if socket[r][c] == 0:
        socket[r][c] = 1
        
        for i in range(4):
            fill(r+dx[i],c+dy[i])
        
        return True

cnt = 0
for r in range(n):
    for c in range(m):
        if fill(r,c) == True:
            cnt += 1