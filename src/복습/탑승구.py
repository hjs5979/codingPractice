def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

g = int(input())
p = int(input())

planes = []

for _ in range(p):
    planes.append(int(input()))

parent = [0] * (g+1)

for i in range(g+1):
    parent[i] = i
cnt = 0
for i in planes:
    if find_parent(parent, i) != 0:
        union_parent(parent,find_parent(parent, i),find_parent(parent, i)-1)
        cnt +=1
    else:
        break

print(cnt)
