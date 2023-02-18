from collections import deque
from itertools import combinations
import copy

n, m = map(int,input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))
    
zeros = []

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            zeros.append((i,j))

combs = list(combinations(zeros,3))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def score(new_data):
    count = 0
    for i in range(n):
        for j in range(m):
            if new_data[i][j] == 0:
                count += 1
    return count
                

# new_data = copy.deepcopy(data)
answer = 0

for comb in combs:
    new_data = copy.deepcopy(data)
    
    for c in comb:
        new_data[c[0]][c[1]] = 1

    q= deque()
        
    for x in range(n):
        for y in range(m):
            if new_data[x][y] == 2:
                q.append((x,y))
    
    while q:
        tempx,tempy = q.popleft()
        
        for i in range(4):
            nx = tempx + dx[i]
            ny = tempy + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if new_data[nx][ny] == 0:
                new_data[nx][ny] = 2
                q.append((nx,ny))

    answer = max(answer, score(new_data))

print(answer)
    
                

        