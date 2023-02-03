n, m = map(int, input().split())

graph = [[1e9] * (n+1) for _ in range(n+1)]
# print(graph)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int,input().split())

# print(graph)

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(n+1):
    for r in range(n+1):
        for c in range(n+1):
            graph[r][c] = min(graph[r][k]+graph[k][c], graph[r][c])

answer = graph[1][k] + graph[k][x]
print( answer if answer < 1e9 else -1)    
    
