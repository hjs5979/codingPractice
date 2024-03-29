def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

graph = []

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))
    # union_parent(parent, a, b)

graph.sort(key = lambda x:x[2])

cost = 0
sum_value = 0
for a,b,c in graph:
    sum_value += c
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        cost += c



print(sum_value-cost)