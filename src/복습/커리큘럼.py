from collections import deque

n = int(input())

array = [[] for _ in range(n+1)]
time = [0] * (n+1)

indegree = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        array[j].append(i)
        indegree[i] += 1
        
# for i in range(1,n+1):
#     for a in array[i]:
#         indegree[i] += 1

q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

result = time.copy()

# print(array)

while q:
    now = q.popleft()
    # print(now)
    for i in array[now]:
        # print(i)
        indegree[i] -= 1
        result[i] = max(result[i], result[now] + time[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1,n+1):
    print(result[i])