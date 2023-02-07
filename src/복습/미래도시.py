n,m = map(int,input().split())

graph = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    graph[i][i] = i

x,k = map(int,input().split())

for z in range(1,n+1): 
    for i in range(1,n+1): 
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][z] + graph[z][j], graph[i][j])

answer = graph[1][k]+graph[k][x]

print(answer if answer < 1e9 else -1)