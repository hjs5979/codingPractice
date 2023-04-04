# from collections import deque

# v, e = map(int, input().split())

# #진입차
# indegree = [0] * (v+1)

# graph = [[] for i in range(v+1)]

# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     indegree[b] += 1

# print(graph)
# print(indegree)

# def topology_sort():
#     result = []
#     q = deque()
    
#     for i in range(1,v+1):
#         if indegree[i] == 0:
#             q.append(i)

#     while q:
#         now = q.popleft()
#         result.append(now)
#         for i in graph[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)
    
#     for i in result:
#         print(i, end=' ')

# topology_sort()

<<<<<<< HEAD
# -------------------------------------------

from collections import deque

v,e = map(int, input().split())

indegree = [0] * (v+1)
=======
# ---------------------------------------------
from collections import deque

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179

indegree = [0] * (n+1)

<<<<<<< HEAD
for i in range(e):
=======
for _ in range(m):
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

<<<<<<< HEAD
result= []

q = deque()

for i in range(v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

print(result)
=======
q = deque()

for i in range(n+1):
    if indegree[i] == 0: 
        q.append(i)
        
while q:
    now = q.popleft()

    print(now)
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
