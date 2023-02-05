def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if b > a:
        parent[b] = a
    else:
        parent[a] = b

def check(parent, a, b):
    if parent[a] == parent[b]:
        return print('yes')
    return print('no')
    
n, m = map(int,input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    c, a, b =map(int,input().split())
    
    if c == 0:
        union_parent(parent, a, b)
        
    if c == 1:
        check(parent, a, b)