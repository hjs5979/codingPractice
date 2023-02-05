import heapq
t = int(input())

for _ in range(t):
    n = int(input())

    graph = []

    for _ in range(n):
        graph.append(list(map(int,input().split())))
    # print(graph)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    distance = [[1e9] * (n) for i in range(n)]

    q = []
    heapq.heappush(q,(0,0,graph[0][0]))
    graph[0][0] = 0

    while q:
        x, y, dist = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                # print(nx,ny)
                cost = dist + graph[nx][ny]
                
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(nx,ny,cost))

    print(distance[n-1][n-1])
    