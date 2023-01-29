from itertools import combinations

n, m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

chicken_list = []
house_list = []

for r in range(n):
    for c in range(n):
        if graph[r][c] == 2:
            chicken_list.append((r,c))

        elif graph[r][c] == 1:
            house_list.append((r,c))
            
        
events = list(combinations(chicken_list,m))

def distance(event):
    chicken_distance = 0
    
    for hx,hy in house_list:
        min_value = 1e9
        for cx,cy in event:
            min_value= min(min_value, abs(hx-cx) + abs(hy-cy))
        chicken_distance += min_value
    return chicken_distance

result = 1e9

for event in events:
    result = min(result, distance(event))

print(result)



    