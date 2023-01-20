temp = input()

alpha = [0,'a','b','c','d','e','f','g','h']

move = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(-2,1),(-2,-1)]

x = alpha.index(temp[0])
y = int(temp[1])

cnt = 0

for dx,dy in move:
    nx,ny = x+dx, y+dy
    if 1<=nx<=8 and 1<=ny<=8:
       cnt += 1

print(cnt)   

