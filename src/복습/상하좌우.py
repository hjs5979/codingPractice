n = int(input())
plans = list(input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

move = ['R','D','L','U']

temp = [0,0]


for i in plans:
    nx = temp[0]+dx[move.index(i)]
    ny = temp[1]+dy[move.index(i)]
    if 0 <= nx <= (n-1) and 0 <= ny <= (n-1):
        temp[0] = nx
        temp[1] = ny
        
print(temp[0]+1, temp[1]+1)