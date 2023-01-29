from collections import deque

n, l, r = map(int, input().split())

graph = []

total_cnt = 0

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(temp, union_num):
    united = []
    united.append(temp)
    queue = deque()
    queue.append(temp)
    union_graph[temp[0]][temp[1]] == union_num
    summary = graph[temp[0]][temp[1]]
    count = 1
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]

            if 0<= nx < n and 0<= ny < n and union_graph[nx][ny] == -1:
                if l <= abs(graph[temp[0]][temp[1]] - graph[nx][ny]) <= r:
                    queue.append((nx,ny))
                    union_graph[nx][ny] = union_num
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i,j in united:
        graph[i][j] = summary // count
    return count


while True:
    union_graph = [[-1] * n for _ in range(n)]
    union_num = 0
    for i in range(n):
        for j in range(n):
            if union_graph[i][j] == -1:
                bfs((i,j), union_num)
                union_num += 1
    if union_num == n*n:
        break
    total_cnt += 1
    
print(total_cnt)