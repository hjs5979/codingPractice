from collections import deque

n, m, k, x = map(int,input().split())

roads = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    roads[a].append(b)

distance = [-1] * (n+1)

distance[x] = 0
queue = deque([x])

answer = []

while queue:
    temp = queue.popleft()
    
    for i in roads[temp]:
        if distance[i] == -1:
            distance[i] = distance[temp] + 1
            queue.append(i)

check = False

for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

    