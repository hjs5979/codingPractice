from itertools import combinations

n, m = map(int, input().split())

street = []

for _ in range(n):
    street.append(list(map(int,input().split())))

chicken = []
house = []

for r in range(n):
    for c in range(n):
        if street[r][c] == 2:
            chicken.append((r,c))
        elif street[r][c] == 1:
            house.append((r,c))

candidates = list(combinations(chicken,m))

def get_sum(candidate):
    result = 0
    for hx,hy in house:
        m = 1e9
        for cx,cy in candidate:
            d = abs(hx-cx) + abs(hy-cy)
            m = min(m,d)
        result += m
    return result

answer = 1e9
for candidate in candidates:
    answer = min(answer, get_sum(candidate))
    
print(answer)    