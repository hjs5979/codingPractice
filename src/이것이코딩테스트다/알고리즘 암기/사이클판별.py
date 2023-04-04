#서로소 집합을 활용한 사이클 판별 소스코드

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
    
# cycle = False

# for i in range(e):
#     a, b = map(int, input().split())
#     if find_parent(parent, a) == find_parent(parent, b):
#         cycle = True
#         break
#     else:
#         union_parent(parent, a, b)
# if cycle:
#     print('occurence of cycle')
# else:
#     print('No occurence of cycle')

#---------------------------------------

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v+1)

cycle = False
for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print(cycle)


