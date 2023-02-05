import heapq

n,m =map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

distance = [1e9] * (n+1)

q = []

heapq.heappush(q,(1,0))
distance[1] = 0

while q:
    now, dist = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = i[1] + dist
        
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(i[0],cost))
            
for i in range(len(distance)):
    if distance[i] == 1e9:
        distance[i] = -1

max_value = max(distance)
cnt = distance.count(max_value)
index = distance.index(max_value)

print(index, max_value, cnt)
        
