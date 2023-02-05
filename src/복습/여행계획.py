def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())

graph = []

route = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

route = list(map(int,input().split()))

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

answer = []

for i in range(m):
    answer.append(find_parent(parent, route[i]))

if len(set(answer)) == 1:
    print('yes')
else:
    print('no')

