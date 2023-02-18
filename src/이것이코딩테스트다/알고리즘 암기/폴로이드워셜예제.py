# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우

# INF = int(1e9)

# n = int(input())
# m = int(input())

# # 2차원 리스트 생성, 모든 값을 무한으로 초기화
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for i in range(n+1):
#     graph[i][i] = 0
    
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# for k in range(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) 

# print(graph)

# -----------------------------------------------------------------------

n = int(input())

m = int(input())

graph = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(n+1):
    for r in range(n+1):
        for c in range(n+1):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])
        