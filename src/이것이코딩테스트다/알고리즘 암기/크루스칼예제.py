# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# v, e = map(int, input().split())
# parent = [0] * (v + 1)

# for i in range(1, v+1):
#     parent[i] = i

# edges = []
# result = 0

# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))

# edges.sort()

# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost

# print(result)

# ------------------------------------------------------------

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

v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i

edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

edges = sorted(edges, key=lambda x:x[2])

cost = 0

for a,b,c in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += c

print(cost)