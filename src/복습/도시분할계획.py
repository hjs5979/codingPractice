def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int,input().split())

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

array = []
for _ in range(m):
    a, b, c = map(int,input().split())
    array.append((a,b,c))

array.sort(key=lambda x:x[2])

cost = 0
max_value = 0

for a,b,c in array:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += c
        max_value = max(c, max_value)

print(cost-max_value)


