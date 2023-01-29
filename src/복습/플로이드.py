n = int(input())
m = int(input())

graph = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0


for _ in range(m):
    a,b,c = map(int,input().split())
    
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1,n+1):
    for r in range(1,n+1):
        for c in range(1,n+1):
            graph[r][c] = min(graph[r][k]+graph[k][c], graph[r][c])

for r in range(1,n+1):
    for c in range(1,n+1):
        if graph[r][c] == 1e9:
            print(0, end=' ')
        else:
            print(graph[r][c], end= ' ')
    print()