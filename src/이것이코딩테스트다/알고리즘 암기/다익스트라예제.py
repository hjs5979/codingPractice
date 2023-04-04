<<<<<<< HEAD
<<<<<<< HEAD
# import heapq
=======
=======
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
# # 개선된 다익스트라 알고리즘

# import heapq
# import sys
<<<<<<< HEAD
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
=======
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179

# INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

# # 노드의 개수, 간선의 개수를 입력 받기
# n, m = map(int, input().split())

# # 시작 노드 번호를 입력받기
# start = int(input())

# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# graph = [[] for i in range(n+1)]

# for _ in range(m):
#     a,b,c, = map(int,input().split())
#     graph[a].append((b,c))
    
# # 최단 거리 테이블을 모두 무한으로 초기화
# distance = [INF] * (n+1)

# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))

# dijkstra(start)

# print(distance)


<<<<<<< HEAD
<<<<<<< HEAD
#---------------------------------------

import heapq

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]
=======
# -------------------------------------------------------
import heapq

n,m = map(int,input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

distance = [1e9] * (n+1)
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179

distance = [1e9] * (n+1)

for i in range(m):
=======
# -------------------------------------------------------
import heapq

n,m = map(int,input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

distance = [1e9] * (n+1)

for _ in range(m):
<<<<<<< HEAD
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
=======
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

q = []

<<<<<<< HEAD
<<<<<<< HEAD
heapq.heappush(q,(start, 0))

distance[start] = 0

while q:
    now, dist = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = i[1] + dist
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(i[0],cost))

print(distance)



=======
=======
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
heapq.heappush(q,(start,0))

while q:
    now, dist = heapq.heappop(q)
    
    if dist > distance[now]:
        continue
    
    for i in graph[now]:
        cost = i[1] + dist
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(i[0],cost))
    
<<<<<<< HEAD
print(distance)
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
=======
print(distance)
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
