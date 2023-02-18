# #개선된 알고리즘

# # 특정 원소가 속한 집합을 찾는 함수
# def find_parent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 노드의 개수와 간선의 개수 입력받기
# v, e = map(int, input().split())
# parent = [0] * (v+1)

# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v+1):
#     parent[i] = i

# # 유니온 연산을 각각 수행
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
# print('각 원소가 속한 집합: ', end='')
# for i in range(1, v+1):
#     print(find_parent(parent, i), end=' ')

# print()

# # 부모테이블 내용 출력
# print('부모 테이블:', end ='')
# for i in range(1, v+1):
#     print(parent[i], end=' ')

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

# -----------------------------------------------------------

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

n, m = map(int,input().split())

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b = map(int,input().split())
    
print(parent)
print(cycle)


    