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
# parent = [0] * (v+1)

# for i in range(1, v+1):
#     parent[i] = i

# -----------------------------------------------------------

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

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    x,y = map(int,input().split())
    union_parent(parent, x, y)

for i in range(1,v+1):
    print(find_parent(parent,i))