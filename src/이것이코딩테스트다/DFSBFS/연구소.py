# 1. 벽세우기
# 2. 바이러스 퍼지기
from itertools import combinations
n, m = map(int, input().split())

place = []

for _ in range(n):
    place.append(list(map(int, input().split())))

p = [[0] * m for _ in range(n)]

# zero = []

# for r in range(m):
#     for c in range(n):
#         if place[r][c] == 0:
#             zero.append((r,c))

# two = []
# for r in range(m):
#     for c in range(n):
#         if place[r][c] == 2:
#             two.append((r,c))

# combs = list(combinations(zero,3))

dx = (0,0,1,-1)
dy = (-1,1,0,0)

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if p[nx][ny] == 0:
                p[nx][ny] = 2
                virus(x, y)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if p[i][j] == 0:
                score += 1
    return score
   
result = 0

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                p[i][j] = place[i][j]
        for i in range(n):
            for j in range(m):
                if p[i][j] == 2:
                    virus(i,j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if place[i][j] == 0:
                place[i][j] = 1
                count += 1
                dfs(count)
                place[i][j] = 0
                count -= 1

dfs(0)
print(result)
            
                

