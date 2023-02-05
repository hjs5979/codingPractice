import heapq

n,m,c = map(int,input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

distance = [1e9] * (n+1)

q = []

heapq.heappush(q, (c,0))
distance[c] = 0

while q:
    now, dist = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = i[1] + dist
        
        if distance[i[0]] > cost:
            distance[i[0]] = cost
        
            heapq.heappush(q,(i[0],cost))

cnt = 0
max_value = 0
for i in distance:
    if i!=0 and i!=1e9:
        cnt += 1
        max_value = max(max_value,i)
        
print(cnt, max_value)
