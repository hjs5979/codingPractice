from collections import deque

tc = int(input())

for t in range(tc):
    n = int(input())
    array = list(map(int,input().split()))
    m = int(input())

    indegree = [0] * (n+1)

    graph = [[False] * (n+1) for i in range(n+1)]

    for i in range(n):
        for j in range(i+1,n):
            graph[array[i]][array[j]] = True
            indegree[array[j]] += 1

    for _ in range(m):
        a, b = map(int,input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []

    q=deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    im = False
    am = False


    for i in range(n):
        if len(q) == 0:
            im = True
            break
        if len(q) >= 2:
            am = True
            break
        
        now = q.popleft()
        result.append(now)
        
        for j in range(1,n+1):
            if graph[now][j] == True:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if im == True:
        print('IMPOSSIBLE')
    elif am == True:
        print('?')
    else:
        for i in result:
            print(i, end= ' ')
    print()