n,m = map(int,input().split())

graph = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    # graph[b][a] = 1

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for r in range(1,n+1):
        for c in range(1,n+1):
            graph[r][c] = min(graph[r][c], graph[r][k]+graph[k][c])
            # if graph[r][k] == 1 and graph[k][c] == 1:
                # graph[r][c] == 1
                # graph[c][r] == 1
            # elif graph[r][k] == -1 and graph[k][c] == -1:
            #     graph[r][c] == -1
            #     graph[c][r] == 1
                
result = 0

for i in range(1, n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != 1e9 or graph[j][i] != 1e9:
            count+=1
        
    if count == n:
        result += 1
        
print(result)
