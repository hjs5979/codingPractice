from itertools import combinations

n,m = map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

zeros = []

for r in range(n):
    for c in range(m):
        if graph[r][c] == 0:
            zeros.append((r,c))

walls = list(combinations(zeros,3))

def contagious(x,y):
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0< nx < n and 0 < ny < m:
            if graph2[nx][ny] == 0:
                graph2[nx][ny] = 2
                contagious(nx,ny)

def count(g):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0:
                cnt +=1
    return cnt 

answer = 0
for wall in walls:
    for a in wall:
        graph2 = graph.copy()
        graph2[a[0]][a[1]] = 1

    for r,c in zeros:
        if graph2[r][c] == 2:
            contagious(r,c)
    
    safe = count(graph2)
    
    answer = max(answer,safe)

print(answer)
            

            
        