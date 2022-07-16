n = int(input())

plan = input().split()

dx = [0,0,-1,1]

dy = [-1,1,0,0]

move = ['L','R','U','D']

x,y = 1,1

for p in plan:
    for i in range(len(move)):
        if p == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx > n or ny > n or nx < 0 or ny < 0:
        continue
    x, y = nx, ny 
        
